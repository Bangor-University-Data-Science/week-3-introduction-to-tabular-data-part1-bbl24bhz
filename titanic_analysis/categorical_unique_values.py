def display_unique_values(df, categorical_features):
    """
    Displays unique values for each categorical feature in the DataFrame.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        categorical_features (list): List of categorical feature names.
    
    Returns:
        dict: A dictionary where keys are feature names and values are the unique values.
    """
   unique_list = df.select_dtypes(include=['object']).columns.to_list()
   unique_values = {}
   for feature in unique_list:
       unique_values[feature] = df[feature].unique()
   return unique_values
