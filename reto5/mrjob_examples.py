from mrjob.job import MRJob
from mrjob.step import MRStep
import re
import pandas as pd
import statistics


class salarios_sector(MRJob):

    def mapper(self, _, line):
        linea = line.split(",")
        if linea[1].isnumeric():
            sector = linea[1]
            salario = linea[2]
            yield(sector, int(salario))


    def reducer(self, sector, salarios):
        listaValores = []
        for salario in salarios:
            listaValores.append(salario)
        yield sector, statistics.mean(listaValores)


class salarios_sector(MRJob):

    def mapper(self, _, line):
        linea = line.split(",")
        if linea[0].isnumeric():
            empleado = linea[0]
            salario = linea[2]
            yield(empleado, int(salario))


    def reducer(self, empleado, salarios):
        listaValores = []
        for salario in salarios:
            listaValores.append(salario)
        yield empleado, statistics.mean(listaValores)


class empleados_sector(MRJob):

    def mapper(self, _, line):
        linea = line.split(",")
        if linea[0].isnumeric():
            empleado = linea[0]
            sector = linea[1]
            yield(empleado, sector )


    def reducer(self, empleado, sectores):
        listaValores = []
        for sector in sectores:
            listaValores.append(sector)
        yield empleado, listaValores


class empresas_max_min(MRJob):

    def mapper(self, _, line):
        linea = line.split(",")
        if linea[1].replace('.','',1).isdigit():
            empresa = linea[0]
            valor_dia = [linea[1], linea[2]]
            yield(empresa, valor_dia )


    def reducer(self, empresa, valores_dia):
        listaValores = []
        for valor_dia in valores_dia:
            if len(listaValores) < 2:
                listaValores.append(valor_dia)
            else:
                if valor_dia > max(listaValores):
                    listaValores.remove(max(listaValores))
                    listaValores.append(valor_dia)
                elif valor_dia < min(listaValores):
                    listaValores.remove(min(listaValores))
                    listaValores.append(valor_dia)
        yield empresa, listaValores


class empresas_estables(MRJob):

    def mapper(self, _, line):
        linea = line.split(",")
        if linea[1].replace('.','',1).isdigit():
            empresa = linea[0]
            valor_dia = [linea[1], linea[2]]
            yield (empresa, valor_dia)

    def reducer(self, empresa, valores_dia):
        flag = True
        listaValores = []
        for valor_dia in valores_dia:
            listaValores.append(valor_dia)
        if len(listaValores) > 2:
            for i in range(len(listaValores) -1):
                if listaValores[i][0] > listaValores[i + 1][0]:
                    flag = False
        if flag:
            yield empresa, listaValores


class dia_negro(MRJob):

    def mapper_get_values(self, _, line):
        linea = line.split(",")
        if linea[0] != "Company":
            empresa = linea[0]
            valor_dia = [float(linea[1]), linea[2]]
            yield (empresa, valor_dia)

    def reducer_gorup_values(self, empresa, valores_dia):
        min = [100000]
        for valor_dia in valores_dia:
            if valor_dia[0] < min[0]:
                min = valor_dia
        yield empresa, min[1]

    # def reducer_find_black(self, _, date_groupes):
    #     yield empresa, fecha


    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_values,
                   reducer=self.reducer_gorup_values),
            #MRStep(reducer=self.reducer_find_black),
        ]


class dia_negro2(MRJob):

    def mapper_get_values(self, _, line):
        linea = line.split(",")
        if linea[0] != "Company":
            fecha = linea[2]
            valor_dia = float(linea[1])
            yield (fecha, valor_dia)

    def reducer_gorup_values(self, fechas, valores_dia):
        listaValores = []
        for valor_dia in valores_dia:
            listaValores.append(valor_dia)
        yield None, (sum(listaValores), fechas )

    def reducer_find_black(self, _, date_groupes):
        yield min(date_groupes)


    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_values,
                   reducer=self.reducer_gorup_values),
            MRStep(reducer=self.reducer_find_black),
        ]


class peliculas_vistas(MRJob):

    def mapper_get_vistas(self, _, line):
        linea = line.split(",")
        if linea[0] != "Usuario":
            usuario = linea[0]
            movies = [linea[1], int(linea[2])]
            yield (usuario, movies)

    def reducer_group_values(self, usuario, movies):
        listaValores = []
        sum = 0
        for movie in movies:
            listaValores.append(movie)
        for i in listaValores:
            sum += i[1]
        prom = sum/len(listaValores)
        yield usuario, [len(listaValores), prom]

# class the_day(MRJob):
#
#     def mapper_get_vistas(self, _, line):
#         linea = line.split(",")
#         if linea[0] != "Usuario":
#             fecha = linea[4]
#             movie = linea[1]
#             yield (fecha, movie)
#
#     def reducer_group_values(self, fecha, movies):
#         listaValores = []
#         for movie in movies:
#             listaValores.append(movie)
#         yield None, (fecha, len(listaValores))
#
#     def reducer_get_max(self, _, values_pairs):
#         yield max(values_pairs)
#
#     def steps(self):
#         return [
#             MRStep(mapper=self.mapper_get_vistas,
#                    reducer=self.reducer_group_values),
#             MRStep(reducer=self.reducer_get_max),
#         ]


class the_day_max(MRJob):

    def mapper_get_vistas(self, _, line):
        linea = line.split(",")
        if linea[0] != "Usuario":
            fecha = linea[4]
            yield (fecha, 1)

    def reducer_group_values(self, fecha, movies):
        yield None, (sum(movies), fecha)

    def reducer_get_max(self, _, values_pairs):
        yield max(values_pairs)

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_vistas,
                   reducer=self.reducer_group_values),
            MRStep(reducer=self.reducer_get_max),
        ]


class the_day_min(MRJob):

    def mapper_get_vistas(self, _, line):
        linea = line.split(",")
        if linea[0] != "Usuario":
            fecha = linea[4]
            yield (fecha, 1)

    def reducer_group_values(self, fecha, movies):
        yield None, (sum(movies), fecha)

    def reducer_get_max(self, _, values_pairs):
        yield min(values_pairs)

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_vistas,
                   reducer=self.reducer_group_values),
            MRStep(reducer=self.reducer_get_max),
        ]



class users_movie(MRJob):

    def mapper_get_vistas(self, _, line):
        linea = line.split(",")
        if linea[0] != "Usuario":
            movie = linea[1]
            user = [linea[0], int(linea[2])]
            yield (movie, user)

    def reducer_group_values(self, movie, users):
        listavalores = []
        sum = 0
        for user in users:
            listavalores.append(user)
        for i in listavalores:
            sum += i[1]
        prom = sum/len(listavalores)
        yield movie, [len(listavalores) , prom]

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_vistas,
                   reducer=self.reducer_group_values),
        ]


class worst_day(MRJob):

    def mapper_get_vistas(self, _, line):
        linea = line.split(",")
        if linea[0] != "Usuario":
            fecha = linea[4]
            rating = int(linea[2])
            yield (fecha, rating)


    def reducer_group_values(self, fecha, ratings):
        yield None, (statistics.mean(ratings), fecha)

    def reducer_get_max(self, _, values_pairs):
        yield min(values_pairs)

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_vistas,
                   reducer=self.reducer_group_values),
            MRStep(reducer=self.reducer_get_max),
        ]


class best_day(MRJob):

    def mapper_get_vistas(self, _, line):
        linea = line.split(",")
        if linea[0] != "Usuario":
            fecha = linea[4]
            rating = int(linea[2])
            yield (fecha, rating)


    def reducer_group_values(self, fecha, ratings):
        yield None, (statistics.mean(ratings), fecha)

    def reducer_get_max(self, _, values_pairs):
        yield max(values_pairs)

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_vistas,
                   reducer=self.reducer_group_values),
            MRStep(reducer=self.reducer_get_max),
        ]


class best_worst(MRJob):

    def mapper_get_vistas(self, _, line):
        linea = line.split(",")
        if linea[0] != "Usuario":
            Genre = linea[3]
            rating =[int(linea[2]),line[1]]
            yield (Genre, rating)


    def reducer_group_values(self, Genre, ratings):
        listaValores = []
        for rating in ratings:
            listaValores.append(rating)
        yield Genre, [max(listaValores), min(listaValores)]


    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_vistas,
                   reducer=self.reducer_group_values),
        ]


if __name__ == '__main__':
    best_worst.run()
