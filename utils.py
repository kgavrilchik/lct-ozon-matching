def process_nan(func):
    def wrapper(a, b, *args, **kwargs):
        if a is None or b is None:
            return None
        return func(a, b, *args, **kwargs)
    return wrapper


def try_cast_to_float(x):
    try:
        return float(x)
    except:
        return None

    
def augment(df):
    cols_to_augment = set(col[:-2] for col in df.columns.tolist() if col.endswith(('_1', '_2')))
    columns_mapping = {
        **{f'{col}_1': f'{col}_2' for col in cols_to_augment},
        **{f'{col}_2': f'{col}_1' for col in cols_to_augment},
        **{'variantid1': 'variantid2', 'variantid2': 'variantid1'}
    }
    return df.rename(columns=columns_mapping)