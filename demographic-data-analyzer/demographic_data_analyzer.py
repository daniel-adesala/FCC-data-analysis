import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df.loc[df['sex']== 'Male', ['age']].mean()
    average_age_men = round(average_age_men[0], 1)
  

    # What is the percentage of people who have a Bachelor's degree?
    percentage = ((df['education'].value_counts().Bachelors)/(df.education.count()))*100
    percentage_bachelors = round(percentage, 1)
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    Advanced = ['Bachelors', 'Masters', 'Doctorate']
    advanced_edu = df.loc[df['education'].isin(Advanced), ['education', 'salary']]
    higher_education = advanced_edu.salary.count()
  
    
    without_advanced_edu = df.loc[~df['education'].isin(Advanced), ['education', 'salary']]
    lower_education = without_advanced_edu.salary.count()

    # percentage with salary >50K
    advabove50 = advanced_edu[advanced_edu['salary'] == '>50K']
    higher_education_rich = round((advabove50['salary'].count() / advanced_edu['salary'].count()) * 100, 1)

    without_advanced_edu = df.loc[~df['education'].isin(Advanced), ['education', 'salary']]
    lower_education_rich = round((without_advanced_edu[without_advanced_edu['salary'] ==         '>50K'].salary.count()/lower_education) * 100, 1)
    

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[df['hours-per-week'] == df['hours-per-week'].min()]
    num_min_workers =min_workers.salary.count()

    
    rich = min_workers[min_workers['salary'] == '>50K'].salary.count()
    rich_percentage = (rich/num_min_workers)*100

    # What country has the highest percentage of people that earn >50K?
    count_value = df.loc[df['salary'] == '>50K', 'native-country'].value_counts()
    tot_val = df['native-country'].value_counts()
    
    highest_earning_country = (count_value/tot_val).idxmax()
  
    highest_earning_country_percentage = round(count_value/tot_val*100, 1)
    highest_earning_country_percentage = highest_earning_country_percentage.max()

    # Identify the most popular occupation for those who earn >50K in India.
     
    above50k = df.loc[df['salary'] == '>50K', ['native-country', 'occupation']]
    above50k = above50k.value_counts()
    in_occ = above50k.loc['India']
    in_occ
    #ind_occ = above50k.loc[above50k['native-country'] == 'India']
    in_occ = in_occ.reset_index(level = 'occupation')#removing level from index
    top_IN_occupation = in_occ[in_occ[0] == in_occ[0].max()].occupation
    top_IN_occupation = top_IN_occupation[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
