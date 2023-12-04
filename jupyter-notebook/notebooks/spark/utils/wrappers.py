def available(func):
    def wrap(*args, **kwargs):
        if args[0]._df is None:
            raise ValueError("Dataframe is empty")
        return func(*args, **kwargs)
    return wrap