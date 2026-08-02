# Laboratorio 2 - Deep Learning (Series de tiempo)



## Correr

```bash
python -m venv venv
./venv/bin/pip install -r requirements.txt
./venv/bin/jupyter notebook notebooks/laboratorio2.ipynb
```

## Estructura

- `notebooks/laboratorio2.ipynb` - LSTM y tuneo, comparación con SARIMA, y catch22 (PCA/clustering)
- `src/preparar_datos.py` - limpieza y armado de las series (genera lo de `data/processed/`)
- `data/raw/` - Excel original, no se modifica
- `data/processed/` - series y split train/test (no se versiona)
