def create_feature_type_dict(df):
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        dict: A dictionary classifying features into numerical and categorical types.
    """
    feature_types = {
        'numerical': {
            'continuous': [],  # Fill with continuous numerical features
            'discrete': []  # Fill with discrete numerical features
        },
        'categorical': {
            'nominal': [],  # Fill with nominal categorical features
            'ordinal': []  # Fill with ordinal categorical features
        }
    }

    num_col = df.select_dtypes(include=['int64', 'float64']).columns
    for c in num_col:
        if df[c].dtype == 'int64':  # Integer columns are often discrete
           feature_types['numerical']['discrete'].append(c)
        else:  # Float columns are typically continuous
           feature_types['numerical']['continuous'].append(c)
   
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    for c in categorical_columns: 
        if c in ['Pclass']:  # Add rules for ordinal features based on known columns
           feature_types['categorical']['ordinal'].append(c)
        else:
           feature_types['categorical']['nominal'].append(c)
    return feature_types
