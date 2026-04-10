from collections import Counter


def channel_counts(df):
    return Counter(df['Channel'])
