# peak-sales-forecasting-system
End-to-end peak sales forecasting system using statistical models, machine learning, and deep learning. Includes feature engineering, time-series cross-validation, and deployment with FastAPI and Docker for real-world decision support.
# Peak Sales Forecasting System

## Overview

This repository contains a complete peak sales forecasting system built using principles from mechanical engineering, applied mathematics, and data science. The project focuses on predicting high-demand periods, seasonal effects, and promotion-driven spikes using time-series models. The work reflects my academic training and project experience at UNISA and CPUT, and my interest in building production-ready forecasting systems.

The system combines classical statistical models, machine learning, and deep learning. The goal is not only accuracy, but also stability, interpretability, and real-world usability.

## Problem Statement

Many businesses struggle to predict peak demand accurately. Poor forecasts lead to stock shortages, overstaffing, or lost revenue. This project models sales as a dynamic system, similar to engineering systems, where trends, seasonality, and external shocks interact over time.

## Data Pipeline

The pipeline follows strict steps to avoid leakage and ensure reliability:

* Raw data ingestion and cleaning
* Handling missing values and outliers
* Time alignment and resampling
* Feature generation based on past information only

## Feature Engineering

I engineered features inspired by signal processing and dynamic systems:

* Lag features (t-1, t-7, t-14, etc.)
* Rolling window statistics (mean, std, min, max)
* Exponential smoothing filters
* Fourier terms for seasonality
* Cyclic encodings (week, month)
* Promotion and impulse indicators

## Models Implemented

The following models are implemented and compared:

* ARIMA / SARIMAX (Statsmodels)
* Prophet (trend and seasonality)
* LightGBM with engineered features
* N-BEATS (deep learning)
* Temporal Fusion Transformer (TFT)

## Evaluation

Models are evaluated using proper time-series cross-validation:

* MAE
* RMSE
* MAPE and SMAPE
* Residual autocorrelation checks
* Probabilistic loss for quantile forecasts

## Deployment

The best-performing model can be deployed using:

* FastAPI for real-time inference
* Pydantic for input validation
* Docker for containerisation
* Optional Streamlit dashboard for visualisation

## Engineering Background

My approach is influenced by mechanical engineering projects, especially system modelling, control logic, and safety constraints. Similar ideas are applied here: stability, robustness, and clear assumptions.

## Tools Used

Python, NumPy, Pandas, Scikit-Learn, LightGBM, XGBoost, Statsmodels, Prophet, PyTorch, PyTorch Lightning, FastAPI, Docker, Streamlit, Git, MATLAB, Simulink.

## Author

Yanga Gcabo
