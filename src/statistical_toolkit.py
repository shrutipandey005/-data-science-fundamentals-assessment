"""
Statistical Toolkit - Pure Python Foundation
Provides fundamental statistical formulas and calculations for Data Science.
Complies with Python standard library (no external dependencies required).
"""

import math
from collections import Counter
from typing import List, Tuple, Union, Optional, Dict


def calculate_mean(data: List[Union[int, float]]) -> float:
    """Computes arithmetic mean: sum(x) / n."""
    if not data:
        raise ValueError("Data list cannot be empty.")
    return sum(data) / len(data)


def calculate_median(data: List[Union[int, float]]) -> float:
    """Computes median: central value of sorted sequence."""
    if not data:
        raise ValueError("Data list cannot be empty.")
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 1:
        return float(sorted_data[mid])
    return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0


def calculate_mode(data: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
    """Computes mode(s): returns list of most frequently occurring values."""
    if not data:
        raise ValueError("Data list cannot be empty.")
    counts = Counter(data)
    max_freq = max(counts.values())
    return [item for item, freq in counts.items() if freq == max_freq]


def calculate_variance(data: List[Union[int, float]], sample: bool = True) -> float:
    """
    Computes variance: sum((x - mean)^2) / degrees_of_freedom.
    If sample=True, uses Bessel's correction (n - 1) for unbiased sample variance.
    If sample=False, uses n for population variance.
    """
    n = len(data)
    if sample and n < 2:
        raise ValueError("Sample variance requires at least 2 data points.")
    if n == 0:
        raise ValueError("Data list cannot be empty.")
    
    avg = calculate_mean(data)
    squared_diffs = sum((x - avg) ** 2 for x in data)
    dof = (n - 1) if sample else n
    return squared_diffs / dof


def calculate_std_dev(data: List[Union[int, float]], sample: bool = True) -> float:
    """Computes standard deviation: square root of variance."""
    return math.sqrt(calculate_variance(data, sample=sample))


def calculate_percentile(data: List[Union[int, float]], percentile: float) -> float:
    """
    Computes p-th percentile (0 <= percentile <= 100) using linear interpolation.
    Equivalent to numpy.percentile method='linear'.
    """
    if not 0 <= percentile <= 100:
        raise ValueError("Percentile must be between 0 and 100.")
    if not data:
        raise ValueError("Data list cannot be empty.")
        
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n == 1:
        return float(sorted_data[0])
    
    # rank index
    index = (percentile / 100.0) * (n - 1)
    lower = int(math.floor(index))
    upper = int(math.ceil(index))
    weight = index - lower
    
    return sorted_data[lower] * (1.0 - weight) + sorted_data[upper] * weight


def calculate_iqr(data: List[Union[int, float]]) -> Tuple[float, float, float]:
    """Returns (Q1, Q3, IQR)."""
    q1 = calculate_percentile(data, 25)
    q3 = calculate_percentile(data, 75)
    return q1, q3, (q3 - q1)


def detect_outliers_iqr(data: List[Union[int, float]], factor: float = 1.5) -> Dict[str, Union[float, List[Union[int, float]]]]:
    """Identifies outliers using Tukey's Fences: [Q1 - 1.5*IQR, Q3 + 1.5*IQR]."""
    q1, q3, iqr = calculate_iqr(data)
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    outliers = [x for x in data if x < lower_bound or x > upper_bound]
    return {
        "q1": q1,
        "q3": q3,
        "iqr": iqr,
        "lower_bound": lower_bound,
        "upper_bound": upper_bound,
        "outliers": outliers
    }


def calculate_covariance(x: List[Union[int, float]], y: List[Union[int, float]], sample: bool = True) -> float:
    """Computes sample or population covariance between two variables."""
    if len(x) != len(y):
        raise ValueError("Lists x and y must have identical lengths.")
    n = len(x)
    if sample and n < 2:
        raise ValueError("Sample covariance requires at least 2 points.")
    
    mean_x = calculate_mean(x)
    mean_y = calculate_mean(y)
    cov_sum = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    dof = (n - 1) if sample else n
    return cov_sum / dof


def calculate_pearson_correlation(x: List[Union[int, float]], y: List[Union[int, float]]) -> float:
    """
    Computes Pearson's r: Cov(x, y) / (Std(x) * Std(y)).
    Measures linear association: -1.0 <= r <= 1.0.
    """
    cov = calculate_covariance(x, y, sample=True)
    std_x = calculate_std_dev(x, sample=True)
    std_y = calculate_std_dev(y, sample=True)
    
    if std_x == 0 or std_y == 0:
        return 0.0  # Zero variance implies zero linear correlation
    return cov / (std_x * std_y)


def bayes_theorem(prior_a: float, prob_b_given_a: float, prob_b_given_not_a: float) -> float:
    """
    Applies Bayes' Theorem: P(A|B) = [P(B|A) * P(A)] / P(B)
    where P(B) = P(B|A)*P(A) + P(B|~A)*(1 - P(A))
    """
    prior_not_a = 1.0 - prior_a
    marginal_b = (prob_b_given_a * prior_a) + (prob_b_given_not_a * prior_not_a)
    if marginal_b == 0:
        raise ValueError("Marginal probability P(B) cannot be zero.")
    return (prob_b_given_a * prior_a) / marginal_b
