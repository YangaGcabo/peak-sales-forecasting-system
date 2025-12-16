data = readtable('sales.csv');
sales = data.sales;

trend = movmean(sales, 12);
plot(sales); hold on;
plot(trend, 'LineWidth', 2);
legend('Raw Sales', 'Smoothed Trend');
