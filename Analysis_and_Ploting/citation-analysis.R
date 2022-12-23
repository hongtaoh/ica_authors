df <- read.csv("../data/processed/papers_to_study_expanded.csv")
df$Year.Distance.from.2022 = abs(df$year - 2022)
cols <- c(1, 16:35)
data <- df[, cols]
model <- lm(gscholar_citation~., data)
summary(model)
