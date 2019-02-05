import pickle

def archive_data(df, name):
    "Stores the data locally as a pickle file"

    pickle.dump(df, open('../data/{}.pkl'.format(name), 'wb'))

    return None
