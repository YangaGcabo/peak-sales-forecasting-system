sales = load('sales.csv');
filtered = movmean(sales(:,2), 7);
plot(filtered)
title('Sales Signal Smoothed Using Engineering Filter')
