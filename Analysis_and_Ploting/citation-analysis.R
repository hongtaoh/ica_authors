library(car)
library(olsrr)

df <- read.csv("../data/processed/papers_to_study_expanded.csv")
df$Year.Distance.from.2022 = abs(df$year - 2022)
df$gscholar_citation_log10 <- log10(df$gscholar_citation + 0.1)
var_cols <- c(1, 16:17, 20:33, 35:36)
data <- df[, var_cols]
model <- lm(gscholar_citation_log10~., data)
summary(model)


vif(model)

## outlier



y_hat <- predict(model)
u <- resid(model)
s_u <- rstandard(model)
qqnorm(s_u)
qqline(s_u, col="red")

plot(y_hat, s_u)
abline(0, 0, col="red")

ols_plot_resid_qq(model)
ols_test_correlation(model)
ols_plot_resid_hist(model)

ols_plot_resid_fit(model)

ols_coll_diag(model)

ols_plot_diagnostics(model)
