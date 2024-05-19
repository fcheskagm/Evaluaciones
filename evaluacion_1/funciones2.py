import numpy as np

class GaussJordan:
    def __init__(self):
        self.matriz = None
        self.n = 0
        self.m = 0

    def set_matriz(self, m):
        self.matriz = np.array(m, dtype=np.float64)
        self.n, self.m = self.matriz.shape

    def get_m(self):
        return self.matriz

    def intercambiar_filas(self, i, j):
        self.matriz[[i, j], :] = self.matriz[[j, i], :]

    def hacer_pivote(self, i):
        pivote = self.matriz[i, i]
        if pivote == 0:
            max_val = np.max(np.abs(self.matriz[i:, i]))
            max_idx = np.where(np.abs(self.matriz[i:, i]) == max_val)[0][0] + i
            if max_val == 0:
                raise ValueError()
            self.intercambiar_filas(i, max_idx)
            pivote = self.matriz[i, i]
        self.matriz[i, :] /= pivote

    def eliminar_por_debajo(self, i):
        for k in range(i+1, self.n):
            factor = self.matriz[k, i]
            self.matriz[k, :] -= factor * self.matriz[i, :]

    def eliminar_por_arriba(self, i):
        for k in range(i-1, -1, -1):
            factor = self.matriz[k, i]
            self.matriz[k, :] -= factor * self.matriz[i, :]

    def eliminacion_hacia_adelante(self):
        for i in range(self.n):
            self.hacer_pivote(i)
            self.eliminar_por_debajo(i)

    def eliminacion_hacia_atras(self):
        for i in range(self.n-1, -1, -1):
            self.eliminar_por_arriba(i)

    def resolver_m(self):
        self.eliminacion_hacia_adelante()
        self.eliminacion_hacia_atras()
        solucion = self.matriz[:, -1]
        rounded_solucion = [round(value, 2) for value in solucion]
        return rounded_solucion
