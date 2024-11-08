from typing import List
import data
from build_data import CountyDemographics


# Part 1: Function to calculate total population for 2014
def population_total(counties: List[CountyDemographics]) -> int:
    # Sum up the population for each county for the year 2014
    return sum(county.population['2014 Population'] for county in counties)


# Part 2: Function to filter counties by state
def filter_by_state(counties: List[CountyDemographics], state: str) -> List[CountyDemographics]:
    # Return a list of counties where the state's name matches the given state
    return [county for county in counties if county.state == state]


# Part 3: Function to calculate total sub-population by education level
def population_by_education(counties: List[CountyDemographics], key: str) -> float:
    # Calculate and return the total sub-population based on the specific education level
    return sum(county.population['2014 Population'] * county.education.get(key, 0) / 100 for county in counties)


# Part 3: Function to calculate total sub-population by ethnicity
def population_by_ethnicity(counties: List[CountyDemographics], key: str) -> float:
    # Calculate and return the total sub-population based on the specific ethnicity
    return sum(county.population['2014 Population'] * county.ethnicities.get(key, 0) / 100 for county in counties)


# Part 3: Function to calculate total sub-population below poverty level
def population_below_poverty_level(counties: List[CountyDemographics]) -> float:
    # Calculate and return the total sub-population living below the poverty level
    return sum(county.population['2014 Population'] * county.income.get('Persons Below Poverty Level', 0) / 100 for county in
        counties)


# Part 4: Function to calculate percent of total population by education level
def percent_by_education(counties: List[CountyDemographics], key: str) -> float:
    # Get the total population and the sub-population by education leve
    total_population = population_total(counties)
    sub_population = population_by_education(counties, key)
    # Calculate and return the percentage
    return (sub_population / total_population) * 100 if total_population > 0 else 0


# Part 4: Function to calculate percent of total population by ethnicity
def percent_by_ethnicity(counties: List[CountyDemographics], key: str) -> float:
    # Get the total population and the sub-population by ethnicity
    total_population = population_total(counties)
    sub_population = population_by_ethnicity(counties, key)
    # Calculate and return the percentage
    return (sub_population / total_population) * 100 if total_population > 0 else 0


# Part 4: Function to calculate percent below poverty level
def percent_below_poverty_level(counties: List[CountyDemographics]) -> float:
    # Get the total population and the sub-population below the poverty level
    total_population = population_total(counties)
    sub_population = population_below_poverty_level(counties)
    # Calculate and return the percentage
    return (sub_population / total_population) * 100 if total_population > 0 else 0


# Part 5: Function to filter counties by education level greater than a threshold
def education_greater_than(counties: List[CountyDemographics], key: str, threshold: float) -> List[CountyDemographics]:
    return [county for county in counties if county.education.get(key, 0) > threshold]
# Filter counties where the education level for the given key is greater than the threshold

# Part 5: Function to filter counties by education level less than a threshold
def education_less_than(counties: List[CountyDemographics], key: str, threshold: float) -> List[CountyDemographics]:
    return [county for county in counties if county.education.get(key, 0) < threshold]
# Filter counties where the education level for the given key is less than the threshold

# Part 5: Function to filter counties by ethnicity greater than a threshold
def ethnicity_greater_than(counties: List[CountyDemographics], key: str, threshold: float) -> List[CountyDemographics]:
    return [county for county in counties if county.ethnicities.get(key, 0) > threshold]
# Filter counties where the percentage of the given ethnicity is greater than the threshold

# Part 5: Function to filter counties by ethnicity less than a threshold
def ethnicity_less_than(counties: List[CountyDemographics], key: str, threshold: float) -> List[CountyDemographics]:
    return [county for county in counties if county.ethnicities.get(key, 0) < threshold]
# Filter counties where the percentage of the given ethnicity is less than the threshold

# Part 5: Function to filter counties with poverty level greater than a threshold
def below_poverty_level_greater_than(counties: List[CountyDemographics], threshold: float) -> List[CountyDemographics]:
    return [county for county in counties if county.income.get('Persons Below Poverty Level', 0) > threshold]
# Filter counties where the poverty level percentage is greater than the threshold

# Part 5: Function to filter counties with poverty level less than a threshold
def below_poverty_level_less_than(counties: List[CountyDemographics], threshold: float) -> List[CountyDemographics]:
    return [county for county in counties if county.income.get('Persons Below Poverty Level', 0) < threshold]
