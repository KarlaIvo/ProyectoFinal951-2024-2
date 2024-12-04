import pandas as pd
import mysql.connector
import os


def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Asdf123',
        database='beauty_creations'
    )


def cargar_datos_csv_a_tabla(csv_file, tabla):
    conn = conectar()
    cursor = conn.cursor()
    file_path = f'C:/Users/mafeh/PycharmProjects/pythonProjectPA/Datasets/{csv_file}'

    if not os.path.exists(file_path):
        print(f"Error: El archivo {file_path} no se encontró.")
        return

    datos = pd.read_csv(file_path)

    cols = ",".join([str(i) for i in datos.columns.tolist()])

    for i, row in datos.iterrows():
        query = f"INSERT INTO {tabla} ({cols}) VALUES ({'%s,' * (len(row) - 1)}%s)"
        cursor.execute(query, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    cargar_datos_csv_a_tabla('Clean_bc_accessories.csv', 'accessories')
    cargar_datos_csv_a_tabla('Clean_bc_bundles.csv', 'bundles')
    cargar_datos_csv_a_tabla('Clean_bc_collabs.csv', 'collabs')
