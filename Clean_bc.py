import pandas as pd

def accesories():
        df = pd.read_csv('proyecto/assets/datasets/beauty_creations_accessories.csv')
        print(len(df))
        #nulos df
        nulls = df.isnull()
        print(nulls.sum() / len(df))

        #duplicados df
        dupli = df[df.duplicated()]
        print(dupli)
        df.drop_duplicates(inplace=True)

        #Normalizacion (z-core) y quitar signo de $, cambiar a numerico
        columna = 'Price'

        if columna in df.columns:
                df[columna] = df[columna].str.replace(r'[\$,]', '', regex=True).astype(float)
                media = df[columna].mean()
                std = df[columna].std()

                df[columna + '_zscore'] = (df[columna] - media) / std

                print(f"Normalización completada para la columna '{columna}' de accessories.")
                print(df[[columna, columna + '_zscore']].head())
        else:
                print(f"La columna '{columna}' no existe en el DataFrame.")

        df.to_csv('proyecto/assets/datasets/Clean_bc_accessories.csv', index=False)

def bundles():
        df1 = pd.read_csv('proyecto/assets/datasets/beauty_creations_bundles.csv')
        print(len(df1))

        # nulos df1
        nulls = df1.isnull()
        print(nulls.sum() / len(df1))

        # duplicados df
        dupli = df1[df1.duplicated()]
        print(dupli)
        df1.drop_duplicates(inplace=True)

        columna = 'Price'

        if columna in df1.columns:
                df1[columna] = df1[columna].str.replace(r'[\$,]', '', regex=True).astype(float)
                media = df1[columna].mean()
                std = df1[columna].std()

                df1[columna + '_zscore'] = (df1[columna] - media) / std

                print(f"Normalización completada para la columna '{columna}' de bundles.")
                print(df1[[columna, columna + '_zscore']].head())
        else:
                print(f"La columna '{columna}' no existe en el DataFrame.")

        df1.to_csv('proyecto/assets/datasets/Clean_bc_bundles.csv', index=False)

def collabs():
        df2 = pd.read_csv('proyecto/assets/datasets/beauty_creations_collabs.csv')
        print(len(df2))

        # nulos df1
        nulls = df2.isnull()
        print(nulls.sum() / len(df2))

        # duplicados df
        dupli = df2[df2.duplicated()]
        print(dupli)
        df2.drop_duplicates(inplace=True)

        columna = 'Price'

        if columna in df2.columns:
                df2[columna] = df2[columna].str.replace(r'[\$,]', '', regex=True).astype(float)
                media = df2[columna].mean()
                std = df2[columna].std()

                df2[columna + '_zscore'] = (df2[columna] - media) / std

                print(f"Normalización completada para la columna '{columna}' de collabs.")
                print(df2[[columna, columna + '_zscore']].head())
        else:
                print(f"La columna '{columna}' no existe en el DataFrame.")

        df2.to_csv('proyecto/assets/datasets/Clean_bc_collabs.csv', index=False)

if __name__ == "__main__":
        accesories()
        bundles()
        collabs()