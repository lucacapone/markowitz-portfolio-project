# 1. Introduction

Portfolio construction is a central problem in finance, because investors rarely evaluate securities in isolation. Instead, they allocate capital across multiple financial assets in order to pursue an investment objective while controlling exposure to uncertainty. A properly structured portfolio provides a systematic criterion for determining the share of wealth to allocate to each asset, avoiding decisions based exclusively on the characteristics of individual securities or on informal assessments.

An essential aspect of portfolio choice is the trade-off between risk and return. In general, investors require higher expected returns as compensation for assuming greater uncertainty about future outcomes. Riskier assets may offer greater profit opportunities, but they also expose investors to larger potential losses and greater performance volatility. Portfolio analysis therefore requires both an estimate of expected return and a measure of risk, so that alternative allocations can be compared consistently.

Diversification plays an important role in managing this relationship. By combining assets whose returns do not move in perfect synchrony, an investor can reduce the overall risk of the portfolio without necessarily reducing expected return in the same proportion. The benefit of diversification depends not only on the riskiness of the individual assets, but also on the covariance and correlation among their returns. Consequently, portfolio construction must consider both the interactions among securities and their respective expected return prospects.

The objective of this project is to analyze six stocks belonging to different sectors and to construct efficient portfolios using Markowitz's mean-variance model. The study applies portfolio theory to a diversified set of equities, estimates return and risk characteristics on the basis of historical data, and provides the theoretical foundation for identifying portfolios that display efficient combinations of expected return and risk.

# 2. Theoretical background

Risky investments are assets whose future returns are uncertain. Common stocks are risky because prices and dividends may vary in response to firm-specific factors, sector conditions, macroeconomic variables, interest rates, investor expectations, and general market dynamics. Since the future payoff is not known with certainty, investors must evaluate both the expected compensation from holding the asset and the variability of possible outcomes around that expectation.

The relationship between risk and return is one of the fundamental principles of financial decision-making. Investors generally expect higher returns when they bear higher levels of risk. However, higher risk does not guarantee higher realized returns; it only indicates greater uncertainty and a wider range of possible outcomes. For this reason, portfolio analysis distinguishes between expected return, which expresses the anticipated average outcome, and risk, commonly measured through the variance or standard deviation of returns.

Risk aversion describes the preference of most investors to avoid unnecessary risk. A risk-averse investor will choose, between two investments with the same expected return, the less risky one. Conversely, the investor will accept additional risk only if the expected return is sufficiently higher to compensate for it. This assumption is central to mean-variance analysis, because it explains why investors seek portfolios that minimize risk for a given expected return or maximize expected return for a given level of risk.

Mean-variance analysis evaluates portfolios using two main quantities: expected return and variance. Expected return represents the average return that the investor expects to obtain from the portfolio, while variance measures the dispersion of returns around that expected value. In this framework, the investor compares portfolios on the basis of expected return and risk, assuming that these dimensions effectively summarize investment performance.

Diversification consists of allocating wealth across multiple assets rather than concentrating the entire investment in a single security. Its objective is to reduce exposure to the specific risk of individual assets. When assets are not perfectly positively correlated, losses or weak returns from one security may be partially offset by better outcomes from another. Therefore, the risk of a diversified portfolio depends both on the volatility of individual assets and on the relationships among their returns.

The expected return of a portfolio is the weighted average of the expected returns of the assets included in the portfolio. If a portfolio contains \(n\) assets, where \(w_i\) is the weight assigned to asset \(i\) and \(E(R_i)\) is the expected return of asset \(i\), the expected return of the portfolio is:

$$
E(R_p) = \sum_{i=1}^{n} w_i E(R_i)
$$

Portfolio variance measures the risk of the overall portfolio. Unlike expected return, it is not simply a weighted average of the variances of the individual assets, but also depends on the covariances among returns. Covariance measures the tendency of two assets to move together. A positive covariance indicates that assets often tend to move in the same direction, whereas a negative covariance indicates frequently opposite movements. Lower covariance among assets increases the potential benefit of diversification.

Using matrix notation, portfolio variance can be expressed as:

$$
\sigma_p^2 = w^T \Sigma w
$$

where \(w\) is the vector of portfolio weights and \(\Sigma\) is the covariance matrix of asset returns. This expression highlights that portfolio risk depends on the entire covariance structure of the assets, and not only on the risk of each security considered separately.

In a fully invested portfolio, the sum of the weights must equal one. This condition ensures that all available capital is allocated among the selected assets:

$$
\sum_{i=1}^{n} w_i = 1
$$

The efficient frontier is the set of portfolios that offer the highest expected return for each level of risk or, equivalently, the lowest risk for each level of expected return. Portfolios located below the efficient frontier are inefficient, because another feasible portfolio exists that offers a higher expected return for the same risk or lower risk for the same expected return. The efficient frontier therefore provides a visual and analytical representation of the best risk-return combinations attainable for a given set of assets.

Markowitz portfolio theory, developed by Harry Markowitz, formalizes portfolio selection through the mean-variance paradigm. It emphasizes that investors should not select assets exclusively on the basis of expected returns or individual risks. Instead, they should evaluate how assets interact within the portfolio through covariance. By combining expected returns, variances, covariances, and constraints on portfolio weights, the Markowitz model identifies efficient portfolios and provides a rigorous basis for modern portfolio construction.

On the basis of this theoretical background, the empirical analysis applies the Markowitz model to six U.S. stocks belonging to different sectors. Historical returns are used to estimate expected returns and the covariance matrix; these estimates then serve as inputs for constructing the efficient frontier, the minimum-variance portfolio, and the maximum Sharpe Ratio portfolio.

# 3. Data collection

The information set used for the analysis consists of historical market data from Yahoo Finance, a source widely used in empirical finance applications for accessing time series of stock prices. The data were collected at daily frequency in order to observe price and return dynamics over time with sufficient detail. The overall time horizon considered covers approximately the last five years, from June 22, 2021 to June 22, 2026. To make the empirical evaluation more rigorous, the most recent month was excluded from the estimation sample: the training sample covers the period from June 22, 2021 to May 29, 2026, while the test sample covers only the period from June 1, 2026 to June 22, 2026. In this way, expected returns, the covariance matrix, correlations, and optimal portfolio weights are estimated only on data available in the training sample, while the final month is used solely for an out-of-sample assessment of realized performance. This separation between the estimation period and the evaluation period avoids the introduction of look-ahead bias, because information from the final month does not contribute to portfolio construction.

Operationally, data collection and preparation were carried out in the script `src/01_download_data.py`, which queries Yahoo Finance through the `yfinance` library at daily frequency and with `auto_adjust=False`, so that the `Adj Close` column can be explicitly extracted. After the joint download of the six tickers, the series are reordered according to a fixed sequence and dates with incomplete observations are removed, so that all securities share the same calendar of comparable returns. The same script saves both the full sample and the training-test split, while also keeping the historical paths `data/raw/adjusted_close_prices.csv` and `data/processed/log_returns.csv` pointed to the training set used in the subsequent analyses.

The sample consists of six stocks listed on the U.S. market: Apple (AAPL), JPMorgan Chase (JPM), Coca-Cola (KO), Johnson & Johnson (JNJ), Exxon Mobil (XOM), and Boeing (BA). The selection of these companies reflects the need to construct a set of assets representative of different economic sectors. Apple belongs to the technology sector, JPMorgan Chase to financials, Coca-Cola to consumer staples, Johnson & Johnson to health care, Exxon Mobil to energy, and Boeing to the aerospace and manufacturing industry. This sectoral heterogeneity is relevant because it reduces the concentration of the analysis in a single area of the economy and makes it possible to assess the potential benefits of diversification more appropriately.

For each security, adjusted closing prices, denoted as *Adjusted Close*, were used. This variable incorporates the effects of corporate events such as dividends, stock splits, and other relevant adjustments, thereby providing a more consistent measure of the return actually attainable by the investor than the simple unadjusted closing price. The use of adjusted prices is particularly important when analyzing historical series over a multi-year horizon, because it avoids distortions in performance measurement.

Daily logarithmic returns were calculated from adjusted prices. If \(P_t\) represents the adjusted price of the security at time \(t\) and \(P_{t-1}\) the adjusted price on the previous trading day, the logarithmic return is defined as:

$$
r_t = \ln\left(\frac{P_t}{P_{t-1}}\right)
$$

Logarithmic returns are preferred in many financial applications because they are additive over time and facilitate the aggregation of returns over longer horizons. In addition, for small price changes, they are very close to simple returns, while offering more convenient analytical properties in statistical modeling and portfolio analysis.

Consistently with this approach, all subsequent descriptive statistics are calculated on daily logarithmic returns from the training set only, as specified in the script `src/02_descriptive_analysis.py`. This choice ensures that the mean, standard deviation, minimum, maximum, skewness, and kurtosis summarize only the information available during the estimation phase, while the final month remains reserved for the out-of-sample assessment.

# 4. Descriptive analysis

Descriptive analysis is an essential preliminary step in the study of financial data, because it summarizes the main empirical characteristics of returns before applying more structured portfolio selection models. Descriptive statistics make it possible to evaluate the average level of returns, dispersion around the mean, the magnitude of observed extremes, and the shape of the distribution. In this way, relevant differences among securities can be identified in terms of historical performance, volatility, and extreme-event risk.

In Figure 1, prices are normalized by setting the initial value of each series equal to 100. This transformation does not alter the relative dynamics of the securities, but removes the effect of different absolute price levels and therefore makes companies with very different initial quotations comparable.

![Normalized prices](../figures/normalized_prices.png)

*Figure 1. Evolution of the normalized prices of the analyzed securities, useful for comparing the relative development of quotations over the observed period on a common base equal to 100.*

## 4.1 Descriptive statistics of returns

| Security | Mean | Standard Deviation | Minimum | Maximum | Skewness | Kurtosis |
|---------|---------|---------|---------|---------|---------|---------|
| AAPL | 0.000703 | 0.017276 | -0.097013 | 0.142617 | 0.248562 | 5.971457 |
| JPM | 0.000658 | 0.015378 | -0.077787 | 0.109254 | -0.049936 | 4.720601 |
| KO | 0.000413 | 0.010108 | -0.072168 | 0.046168 | -0.269165 | 3.871000 |
| JNJ | 0.000372 | 0.010613 | -0.078953 | 0.060090 | -0.010907 | 5.034804 |
| XOM | 0.000813 | 0.016823 | -0.082136 | 0.062142 | -0.316088 | 1.492777 |
| BA | -0.000043 | 0.023039 | -0.110608 | 0.143010 | -0.150880 | 3.490003 |

The table of descriptive statistics should be read as a joint summary of average return, risk, and the distributional shape of daily logarithmic returns. The mean indicates the direction of average historical performance, the standard deviation measures daily volatility, the minimum and maximum identify the observed extreme shocks, while skewness and kurtosis help assess asymmetry and tail weight. The reported statistics reveal significant heterogeneity among the daily returns of the six securities. In terms of average return, Exxon Mobil has the highest value, equal to 0.000813, indicating the most favorable average daily performance in the sample considered. Apple and JPMorgan Chase also show positive and relatively high average returns, equal to 0.000703 and 0.000658, respectively. Coca-Cola and Johnson & Johnson record lower but still positive average returns, consistently with the more defensive nature of their respective sectors. Boeing, by contrast, has a negative average return, equal to -0.000043, indicating that during the observed period the stock had a lower average daily performance than the other instruments analyzed.

The standard deviation makes it possible to compare the degree of return volatility. Boeing is the most volatile stock, with a standard deviation equal to 0.023039, indicating greater instability in daily returns and broader exposure to specific risk. Apple, Exxon Mobil, and JPMorgan Chase display intermediate levels of volatility, while Coca-Cola and Johnson & Johnson have the lowest standard deviations, equal to 0.010108 and 0.010613, respectively. This evidence is consistent with the defensive profile of consumer staples and health care, which tend to be less sensitive to cyclical fluctuations than sectors more exposed to economic conditions.

The minimum and maximum values confirm the presence of substantial daily fluctuations, especially for securities characterized by higher risk. Boeing shows both a very negative minimum, equal to -0.110608, and a high maximum, equal to 0.143010, indicating a particularly wide return distribution. Apple also displays a very high maximum, equal to 0.142617, accompanied by volatility higher than that of defensive stocks. Exxon Mobil, while recording the highest average return, has significant volatility, although lower than Boeing's; this suggests relatively strong historical performance, albeit accompanied by non-negligible exposure to energy-sector risk.

Skewness provides information on the asymmetry of the return distribution. Apple has positive skewness, indicating a higher relative probability of observing extremely positive returns than extremely negative returns. The other securities show negative values or values close to zero. JPMorgan Chase and Johnson & Johnson have very limited asymmetries, suggesting almost symmetric distributions. Coca-Cola, Exxon Mobil, and Boeing instead record negative skewness, which may be interpreted as a greater relative incidence of extreme observations in the left tail of the distribution, that is, particularly pronounced daily losses.

Kurtosis measures the degree of concentration of the distribution and the relevance of the tails relative to a normal distribution. The positive and relatively high values observed for Apple, Johnson & Johnson, and JPMorgan Chase indicate leptokurtic distributions, characterized by heavier tails and therefore by a higher probability of extreme returns. Coca-Cola and Boeing also have kurtosis values above zero, confirming that extreme events are not negligible. Exxon Mobil shows lower kurtosis than the other securities, while still maintaining a distribution that is not perfectly comparable to a normal distribution.

Overall, the descriptive results have relevant implications for portfolio construction. Securities with higher average returns, such as Exxon Mobil, JPMorgan Chase, and Apple, may contribute to increasing the portfolio's expected return, but they must be evaluated jointly with their volatility and the shape of their return distribution. More defensive securities, such as Coca-Cola and Johnson & Johnson, while offering lower average returns, may contribute to portfolio stabilization through lower volatility. Boeing, given its combination of negative average return and high volatility, requires particular attention during the allocation phase, because it may increase overall risk without offering an adequate contribution to expected return. This evidence confirms the importance of combining assets with different characteristics, so that portfolio selection accounts not only for average performance, but also for variability, asymmetry, and the probability of extreme events.

The daily logarithmic return series shown in Figure 2 make it possible to directly observe daily shocks, that is, sudden changes of substantial magnitude relative to the normal fluctuation of the securities. The concentration of large movements in certain time intervals also indicates return volatility and the possible presence of volatility clusters, in which turbulent days tend to be followed by other days characterized by strong instability.

![Daily logarithmic returns](../figures/log_returns.png)

*Figure 2. Series of daily logarithmic returns, used to assess volatility, extreme fluctuations, and differences in behavior among the securities.*

# 5. Correlation analysis

Correlation analysis is a fundamental step in portfolio theory, because it makes it possible to evaluate the extent to which the returns of financial assets tend to move together. In the context of diversification, it is not sufficient to consider the average return and volatility of each security separately: the statistical relationships among the assets included in the portfolio must also be examined. Two securities characterized by high individual risk may in fact generate an overall less risky portfolio if their returns do not move in perfect synchrony.

The correlation coefficient measures the strength and direction of the linear relationship between two return series. It takes values between -1 and +1. A value equal to +1 indicates perfect positive correlation, namely a tendency for the two returns to vary in the same direction and in constant linear proportion. A value equal to -1 indicates perfect negative correlation, that is, a tendency for returns to move in opposite directions. A value close to zero instead indicates a weak or absent linear relationship, while not necessarily excluding other forms of statistical dependence.

Positive correlation occurs when two assets tend to record high or low returns in the same period. In this situation, the diversification benefit is more limited, because adverse shocks may affect both assets simultaneously. Negative correlation, by contrast, indicates that the returns of one asset tend to increase when those of the other decrease. This relationship is particularly relevant for risk reduction, because the losses of one security may be offset, at least in part, by the gains of the other.

In the Markowitz framework, low or negative correlations are essential because they allow the overall variance of the portfolio to be reduced for given individual expected returns. Mean-variance logic shows that portfolio risk depends not only on the variances of individual securities, but also on covariances, which are directly related to correlations. Therefore, selecting assets with low correlations allows more efficient combinations to be constructed, improving the risk-return profile relative to an investment concentrated in highly correlated securities.

The empirical estimation of the relationships among securities was carried out in the script `src/03_correlations.py` using logarithmic returns from the training set. In particular, the matrix reported below is a Pearson correlation matrix, obtained by applying the `pearson` method to the daily return series. This choice is consistent with the mean-variance model, because it measures linear dependence among assets and provides information directly related to the covariance matrix used in the subsequent portfolio optimization.

## 5.1 Correlation matrix

|      | AAPL | JPM | KO | JNJ | XOM | BA |
|------|------|------|------|------|------|------|
| AAPL | 1.000 | 0.375 | 0.257 | 0.151 | 0.183 | 0.382 |
| JPM  | 0.375 | 1.000 | 0.203 | 0.189 | 0.301 | 0.404 |
| KO   | 0.257 | 0.203 | 1.000 | 0.451 | 0.166 | 0.132 |
| JNJ  | 0.151 | 0.189 | 0.451 | 1.000 | 0.118 | 0.073 |
| XOM  | 0.183 | 0.301 | 0.166 | 0.118 | 1.000 | 0.204 |
| BA   | 0.382 | 0.404 | 0.132 | 0.073 | 0.204 | 1.000 |

The correlation matrix table should be interpreted by jointly comparing the sign and magnitude of the coefficients: the main diagonal is equal to 1 because each security is perfectly correlated with itself, while off-diagonal elements indicate the degree of linear co-movement between pairs of securities. Higher values reduce the potential benefit of diversification, while values close to zero suggest more independent movements. The correlation matrix shows that all relationships among the securities considered are positive, but generally limited. The highest correlation is observed between Coca-Cola (KO) and Johnson & Johnson (JNJ), equal to 0.451. This value indicates a moderate positive relationship between two securities belonging to defensive sectors, consumer staples and health care, respectively. Although it is the highest correlation in the sample, it remains far from values close to unity and therefore does not indicate an almost perfect overlap in return movements.

The lowest correlation is recorded between Johnson & Johnson (JNJ) and Boeing (BA), equal to 0.073. This value, very close to zero, suggests an extremely weak linear relationship between the returns of the two securities. From a diversification perspective, this evidence is relevant because it indicates that Boeing's movements, as an industrial and aerospace stock characterized by higher volatility, are only weakly associated with the movements of Johnson & Johnson, a company belonging to a more defensive sector.

A particularly significant element is the absence of very high correlations among the selected assets. No pair of securities has values close to 0.80 or 0.90, thresholds that would indicate strong linear dependence and a consequent reduction in diversification benefits. Even the relatively higher correlations, such as JPMorgan Chase (JPM) with Boeing (BA), equal to 0.404, and Apple (AAPL) with Boeing (BA), equal to 0.382, remain at moderate levels.

These results confirm the presence of diversification benefits within the universe of securities considered. The combination of firms belonging to different sectors makes it possible to reduce exposure to shocks specific to individual companies or economic segments. The limited correlations indicate that returns do not move in a perfectly coordinated manner, making it possible to reduce overall risk through an appropriate choice of portfolio weights.

Overall, the correlation structure suggests that the selected securities are appropriate for the subsequent construction of portfolios according to the Markowitz approach. Sectoral heterogeneity and the absence of excessively high linear relationships provide a favorable empirical basis for mean-variance analysis. The matrix is also represented graphically in the correlation heatmap generated during the analysis, saved in the file `figures/correlation_heatmap.png`, which makes it possible to visualize the relative intensity of the relationships among the securities' returns immediately.

In Figure 3, colors and numerical values jointly represent the intensity and direction of Pearson correlations: stronger shades and values farther from zero indicate stronger linear relationships, while the sign of the coefficient distinguishes movements in the same direction from movements in opposite directions.

![Correlation heatmap](../figures/correlation_heatmap.png)

*Figure 3. Heatmap of the return correlation matrix, highlighting the prevalence of positive but moderate relationships among the assets considered.*


## 5.2 Statistical significance of correlations


To complete the descriptive analysis of the correlation matrix, the **statistical significance** of the Pearson correlation coefficients was also evaluated.

The correlation matrix makes it possible to observe **how much two securities tend to move together**, but by itself it does not establish whether the observed relationship is actually significant or whether it could be due to chance.

For this reason, a statistical test on the Pearson correlation coefficient was performed for each pair of securities. In the script `src/03_correlations.py`, the p-value matrix is constructed by applying `scipy.stats.pearsonr` to each pair of logarithmic return series; the first value returned by the function corresponds to the correlation coefficient, while the second is the p-value associated with the test of no linear correlation.

The null hypothesis of the test is:

$$
H_0: \rho = 0
$$

where \(\rho\) represents the population correlation.
The null hypothesis therefore states that **there is no significant linear relationship between the returns of the two securities**.

For each pair of securities, the sample correlation coefficient, denoted by \(r\), is calculated. This coefficient is then transformed into the following test statistic:

$$
t = r \sqrt{\frac{n-2}{1-r^2}}
$$

where \(n\) indicates the number of available observations, that is, the number of daily returns in the training sample.

The \(t\) statistic is compared with a **Student's t distribution** with \(n-2\) degrees of freedom. The corresponding **p-value** is calculated from this distribution.

The **p-value** indicates how compatible the observed correlation coefficient is with the null hypothesis of no correlation. A low p-value indicates low compatibility with this hypothesis and therefore leads the correlation to be considered statistically significant.

If the p-value is below a given significance level, for example **5%**, the null hypothesis is rejected and the correlation between the two securities is concluded to be **statistically significant**.

Conversely, a high p-value does not allow the null hypothesis to be rejected, indicating that there is insufficient statistical evidence to claim the existence of a linear correlation different from zero.

## Joint interpretation of correlations and p-values

The p-value matrix complements the information provided by the correlation matrix and the corresponding heatmap.

The **correlation heatmap** shows:

- the **sign** of the linear relationship between returns;
- the **intensity** of the relationship;
- the direction of the joint movement of the securities.

In particular:

- positive values indicate that securities tend to move in the same direction;
- negative values indicate that securities tend to move in opposite directions;
- values close to zero indicate a weak linear relationship.

The **p-value matrix**, instead, makes it possible to verify whether these relationships are statistically significant.

Consequently, the two matrices must be interpreted together:

- the correlation matrix describes **how strong and in which direction** the relationship among securities is;
- the p-value matrix evaluates **how statistically reliable** that relationship is.

The formatted p-value matrix is as follows. Each cell should be read as the statistical evidence associated with the corresponding pair of securities in the correlation matrix: very small values indicate that the estimated coefficient is unlikely to be compatible with the null hypothesis of no linear correlation, but they do not measure the economic importance of the relationship. For this reason, the p-value table reinforces, but does not replace, the interpretation of the correlation coefficients.


|      | AAPL | JPM | KO | JNJ | XOM | BA |
|------|------|------|------|------|------|------|
| AAPL | <0.001 | <0.001 | <0.001 | <0.001 | <0.001 | <0.001 |
| JPM  | <0.001 | <0.001 | <0.001 | <0.001 | <0.001 | <0.001 |
| KO   | <0.001 | <0.001 | <0.001 | <0.001 | <0.001 | <0.001 |
| JNJ  | <0.001 | <0.001 | <0.001 | <0.001 | <0.001 | 0.012 |
| XOM  | <0.001 | <0.001 | <0.001 | <0.001 | <0.001 | <0.001 |
| BA   | <0.001 | <0.001 | <0.001 | 0.012 | <0.001 | <0.001 |

The results show that almost all p-values are below 0.001, indicating strong statistical evidence against the hypothesis of zero correlation. The only relative exception is the JNJ--BA pair, for which the p-value is equal to 0.012: this value is nevertheless below the 5% threshold, so the correlation is statistically significant.
However, the estimated coefficient is very low, equal to about 0.071, and should be interpreted as economically weak. Small p-values therefore lead to rejection of \(H_0\) and indicate that the observed correlation is statistically significant.

It is important to emphasize that a statistically significant correlation is not necessarily economically relevant.

Indeed, when the number of observations is large, the statistical test may identify even very low correlations as significant. In these cases, the p-value may be small and lead to rejection of the null hypothesis, but the relationship between the two securities may still be weak and of limited practical usefulness.

For this reason, statistical significance must be interpreted together with the value of the correlation coefficient. The p-value indicates whether the correlation is statistically different from zero, while the correlation coefficient indicates how strong the relationship between returns is.

Consequently, a correlation may be statistically significant but have a limited economic impact if the value of \(r\) is close to zero.
# 6. Application of the Markowitz model

The empirical application of the Markowitz model first requires the transformation of historical adjusted price series into daily returns and the subsequent estimation of the fundamental parameters of mean-variance analysis. The expected return of each security was estimated as the arithmetic mean of daily returns observed in the sample. This quantity represents a summary measure of average historical performance and constitutes the starting point for calculating the expected return of each feasible portfolio.

The entire simulation and optimization procedure is implemented in the script `src/04_markowitz_simulation.py`, which uses as input the logarithmic returns from the training set saved in `data/processed/log_returns.csv`. Before optimization, the script verifies that all expected tickers are present and reorders them consistently, so as to maintain the same correspondence among the weight vector, expected returns, and covariance matrix. This phase is methodologically relevant because the Markowitz model is sensitive to the alignment between assets and estimated parameters.

Since the analysis is expressed on an annual basis, average daily returns were annualized assuming 252 trading days in a year. Denoting the average daily return by \(\mu_{daily}\), the expected annual return was calculated according to the following relationship:

$$
\mu_{ann} = 252 \cdot \mu_{daily}
$$

The second essential component of the model is the covariance matrix of returns. It was estimated from the daily return series of the six securities considered and makes it possible to incorporate not only the individual volatility of each asset, but also the degree of co-movement among the different financial assets. In the Markowitz model, in fact, the overall risk of the portfolio depends on the covariance matrix and on the weights assigned to the securities, according to the relationship \(\sigma_p^2 = w^T \Sigma w\). The daily covariance matrix was therefore annualized by multiplying it by 252, consistently with the daily frequency of the data.

For each portfolio, daily volatility was obtained as the standard deviation of portfolio returns. This measure was also expressed on an annual basis using the square root of the number of trading days. Denoting daily volatility by \(\sigma_{daily}\), annual volatility was calculated as:

$$
\sigma_{ann} = \sqrt{252} \cdot \sigma_{daily}
$$

Subsequently, 10,000 random portfolios were simulated. For each simulation, a vector of weights assigned to the six securities was generated, imposing that the sum of the weights equal one. In addition, short selling was excluded: consequently, each portfolio weight is constrained to lie between 0 and 1. Formally, the imposed constraints are \(\sum_{i=1}^{n} w_i = 1\) and \(0 \leq w_i \leq 1\) for every asset \(i\). These conditions describe a long-only portfolio, in which the investor may hold only positive or zero positions in the securities considered.

For each simulated portfolio, annual expected return, annual volatility, and the Sharpe Ratio were calculated. In this analysis, the risk-free rate is assumed to be zero; therefore, the Sharpe Ratio measures expected return per unit of total risk borne. Denoting the expected return of the portfolio by \(\mu_p\) and its volatility by \(\sigma_p\), the indicator is defined as:

$$
SR = \frac{\mu_p}{\sigma_p}
$$

The efficient frontier was constructed by identifying, among feasible combinations, the portfolios that have the minimum level of volatility for each expected return or, equivalently, the maximum expected return for each level of risk. The efficient frontier therefore represents the set of dominant allocations in the risk-return plane. Portfolios located below it are inefficient, because alternative combinations exist that can offer a higher return for the same volatility or lower volatility for the same expected return.

From a computational perspective, the 10,000 random portfolios constitute a simulated representation of the space of long-only allocations and make it possible to identify, among the generated simulations, the minimum-variance portfolio and the maximum Sharpe Ratio portfolio. The efficient frontier, instead, is not obtained simply by connecting the simulated points, but is calculated through constrained optimization using the SLSQP method: for a grid of target returns, the algorithm minimizes volatility while simultaneously respecting the full-investment constraint and the bounds \(0 \leq w_i \leq 1\). The out-of-sample assessment finally uses the same weights estimated on the training set, without recalibrating them on the test-month data.

# 7. Results

The minimum-variance portfolio and the maximum Sharpe Ratio portfolio are identified among the 10,000 random portfolios simulated in `src/04_markowitz_simulation.py`, through the function `find_extreme_portfolios`, while the efficient frontier is constructed through constrained optimization in the function `build_efficient_frontier`.

## 7.1 Minimum-variance portfolio

The minimum-variance portfolio represents the allocation that, among feasible allocations, achieves the lowest overall volatility. The estimated results for this portfolio are as follows:

- Annualized expected return = 11.38%
- Annualized volatility = 12.73%
- Sharpe Ratio = 0.894

The composition of the minimum-variance portfolio is reported below. This weight table shows how the optimization translates estimates of volatility and covariance into operational shares: higher weights indicate assets that contribute more to reducing overall risk, while lower weights identify securities that are less useful for minimizing variance given the set of constraints.


- AAPL = 5.63%
- JPM = 3.55%
- KO = 37.79%
- JNJ = 34.90%
- XOM = 12.91%
- BA = 5.22%

The weight structure highlights a strong relative concentration in Coca-Cola and Johnson & Johnson. This result is consistent with the empirical characteristics observed in the previous sections: both securities have lower daily volatility than the other assets in the sample and belong to traditionally defensive sectors, consumer staples and health care, respectively. In a variance-minimization problem, assets characterized by lower return instability naturally tend to receive higher weights, especially when they make it possible to reduce overall risk without excessively compromising expected return.

The high weight assigned to KO and JNJ should not be interpreted only as a consequence of their low individual volatility, but also in light of their covariance relationships with the other securities. Although the correlation between KO and JNJ is the highest among those observed in the sample, it remains moderate and does not eliminate the benefits of diversification. Their inclusion with substantial weights therefore contributes to stabilizing the portfolio, offsetting exposure to more cyclical or more volatile securities such as AAPL, JPM, XOM, and BA.

## 7.2 Maximum Sharpe Ratio portfolio

The maximum Sharpe Ratio portfolio is the allocation that maximizes expected return per unit of risk, assuming a risk-free rate equal to zero. It does not necessarily coincide with the least risky portfolio, because the objective is to improve the relationship between return and volatility. The results obtained are as follows:

- Annualized expected return = 14.97%
- Annualized volatility = 14.00%
- Sharpe Ratio = 1.069

The composition of the maximum Sharpe Ratio portfolio is as follows. In this case, the weight table should not be read as a simple ranking of average returns, but as the result of the trade-off among contribution to expected return, individual volatility, and diversification capacity relative to the other securities.


- AAPL = 15.68%
- JPM = 14.75%
- KO = 19.22%
- JNJ = 22.98%
- XOM = 27.31%
- BA = 0.08%

Compared with the minimum-variance portfolio, this allocation assigns a higher weight to securities with greater contribution to expected return, particularly Exxon Mobil, Apple, and JPMorgan Chase. XOM receives the largest weight, consistently with the highest average return observed in the sample. At the same time, the portfolio retains a relevant share in KO and JNJ, which continue to play a stabilizing role in overall volatility.

Boeing is almost excluded from the maximum Sharpe Ratio portfolio, with a weight equal to 0.08%. This result reflects the unfavorable combination of negative historical average return and high volatility. From a mean-variance perspective, a security with high return dispersion may be included only if it offers an adequate contribution to expected return or sufficiently relevant diversification benefits. In the case of BA, these benefits are not sufficient to offset the unfavorable risk-return profile; consequently, the optimization tends to assign it an almost zero weight.

## 7.3 Comparison between simulated and optimized portfolios

The initial portfolio selection was performed by simulating 10,000 feasible random portfolios. In this approach, weights are generated randomly, normalized so that their sum equals one, and constrained to the interval $0 \leq w_i \leq 1$, thus excluding short selling. The minimum-variance portfolio and maximum Sharpe Ratio portfolio discussed in the previous sections derive from this simulated exploration of the allocation space.

As an additional robustness check, the same two portfolios were also calculated through direct numerical optimization. For the optimized minimum-variance portfolio, the following problem was solved:

$$
\min_w \quad w^T \Sigma w
$$

subject to:

$$
\sum_{i=1}^{n} w_i = 1
$$

$$
0 \leq w_i \leq 1
$$

For the optimized maximum Sharpe Ratio portfolio, assuming a risk-free rate equal to zero consistently with the rest of the analysis, the negative Sharpe Ratio was minimized:

$$
\min_w \quad - \frac{w^T \mu}{\sqrt{w^T \Sigma w}}
$$

subject to:

$$
\sum_{i=1}^{n} w_i = 1
$$

$$
0 \leq w_i \leq 1
$$

The main difference between the two approaches is computational. The simulation searches for the best solution among 10,000 randomly generated feasible portfolios and therefore provides an approximate solution. Optimization, instead, directly solves the constrained mathematical problem and tends to produce a numerically more precise solution, while remaining subject to the same assumptions regarding expected returns, the covariance matrix, and long-only constraints.

The following table reports the comparison saved in `outputs/portfolios/portfolio_optimization_comparison.csv`.

| Portfolio                   | Return   | Volatility | Sharpe Ratio | AAPL weight | JPM weight | KO weight | JNJ weight | XOM weight | BA weight |
| --------------------------- | -------- | ---------- | ------------ | ----------- | ---------- | --------- | ---------- | ---------- | --------- |
| Simulation Minimum Variance | 0.113770 | 0.127310   | 0.893648     | 0.056262    | 0.035482   | 0.377921  | 0.349045   | 0.129126   | 0.052164  |
| Optimized Minimum Variance  | 0.119207 | 0.126561   | 0.941894     | 0.056167    | 0.097946   | 0.346187  | 0.356417   | 0.116558   | 0.026725  |
| Simulation Maximum Sharpe   | 0.149680 | 0.140006   | 1.069098     | 0.156755    | 0.147452   | 0.192153  | 0.229768   | 0.273105   | 0.000767  |
| Optimized Maximum Sharpe    | 0.148773 | 0.138835   | 1.071586     | 0.150177    | 0.151965   | 0.240818  | 0.195368   | 0.261672   | 0.000000  |

The results show that the optimized portfolios are overall close to those identified through simulation, but they do not coincide perfectly. For the minimum-variance portfolio, optimization produces slightly lower volatility than simulation, as expected, because the algorithm directly searches for the variance minimum in the feasible space instead of limiting itself to randomly drawn portfolios. In the case of the maximum Sharpe Ratio as well, the optimized Sharpe Ratio is slightly higher than the one obtained from simulation, confirming that the numerical procedure can improve or at least match the best solution found randomly.

The observed differences depend on the fact that simulation considers a finite number of random combinations: even with 10,000 portfolios, there is no guarantee that one of the simulated points will coincide exactly with the mathematical optimum. Optimization is therefore useful as a check on the quality of the simulated results and makes it possible to evaluate how close the random solutions are to the constrained optima. Both approaches are consistent with the Markowitz framework, because they use the same inputs, the same full-investment and no-short-selling constraints, and measure portfolios in terms of expected return, volatility, and Sharpe Ratio.

## 7.4 Efficient frontier

The efficient frontier graphically summarizes the relationship between risk and expected return for the set of feasible portfolios. In the risk-return plane, each portfolio is represented by a pair consisting of annual volatility and annual expected return. In general, portfolios with higher expected return require the assumption of greater risk, while portfolios with lower volatility tend to offer lower expected returns. However, the relationship is not mechanical, because diversification makes it possible to modify overall risk through the combination of assets that are not perfectly correlated.

The interpretation of the efficient frontier is based on the principle of mean-variance dominance. Portfolios located on the frontier are efficient because, for a given level of volatility, no other allocation can offer a higher expected return; similarly, for a given level of expected return, no portfolio has lower volatility. Portfolios located below the frontier are instead inefficient, because they are dominated by more favorable alternative combinations.

The benefits of diversification emerge from the fact that portfolio volatility is not a simple weighted average of individual volatilities, but also depends on the covariances among returns. The presence of limited correlations among the selected securities makes it possible to construct portfolios with lower risk than would be obtained by concentrating the investment in individual assets. In particular, the inclusion of defensive securities such as KO and JNJ contributes to reducing overall variability, while securities such as XOM, AAPL, and JPM can increase expected return when included with weights consistent with the risk constraints.

Operationally, the efficient frontier was constructed in the script `src/04_markowitz_simulation.py` through constrained optimization with the SLSQP method. The script uses as input the logarithmic returns contained in `data/processed/log_returns.csv`, annualizes average returns and the covariance matrix, and initially generates 10,000 random long-only portfolios. For each simulated portfolio, annualized expected return, annualized volatility, and the Sharpe Ratio are calculated.

Random simulation serves to explore the space of feasible portfolios and to visualize many possible combinations of risk and return. However, because it is a random sampling procedure, it does not necessarily guarantee identification of the exact mathematical optimum. For this reason, the efficient frontier is constructed separately through constrained optimization. In particular, for each target expected return level, the SLSQP algorithm minimizes portfolio volatility while respecting the full-investment and long-only constraints, namely weights summing to one and weights between 0 and 1.

Formally, for each target return, the following problem is solved:

$$ \min_w \quad w^T \Sigma w $$

subject to:

$$ w^T \mu = \mu_{target} $$

$$ \sum_i w_i = 1, \qquad 0 \leq w_i \leq 1 $$

The set of portfolios obtained for the different target return levels constitutes the efficient frontier. Consequently, while the 10,000 simulated portfolios provide an approximate description of the space of possible allocations, the efficient frontier derives from a more structured numerical optimization procedure.

The figure `figures/efficient_frontier.png` represents the efficient frontier generated by the analysis. It makes it possible to visually compare the 10,000 simulated portfolios with the efficient allocations. The updated chart also includes a horizontal line starting from the minimum-variance portfolio: this visual reference separates the upper region, where efficient combinations with expected return at least equal to that of the minimum-variance portfolio are located, from the lower region, associated with inefficient portfolios because they are dominated in terms of expected return for the same or almost the same risk. Random portfolios occupy a wider area of the risk-return plane and include many suboptimal combinations; the efficient frontier, instead, identifies the upper boundary of this set, that is, the combinations offering the best available opportunities. The comparison between simulated portfolios and efficient portfolios therefore shows how Markowitz optimization makes it possible to select superior allocations relative to random choices of weights, while maintaining the constraints of no short selling and weights between 0 and 1.

In the chart in Figure 4, the scattered points represent random portfolios simulated by choosing different long-only weight combinations, while the red curve represents the efficient frontier obtained through optimization. The special points highlight the minimum-variance portfolio and the maximum Sharpe Ratio portfolio; the horizontal line, drawn from the return of the minimum-variance portfolio, helps visually distinguish the efficient region, located on the upper segment of the frontier, from combinations that are dominated or less interesting from a mean-variance perspective.

![Efficient frontier](../figures/efficient_frontier.png)

*Figure 4. Efficient frontier of simulated portfolios, with a horizontal line from the minimum-variance portfolio and a visual distinction between the efficient and inefficient regions.*



## 7.5 Out-of-sample assessment over the last month

The separation between the training sample and the test sample makes it possible to evaluate whether the optimal portfolios, constructed using only information available up to May 29, 2026, maintain consistent performance also in the following month, which was excluded from estimation. The out-of-sample assessment is conducted over the period from June 1, 2026 to June 22, 2026, equal to 14 trading days, comparing the expected simple monthly return with the actually realized simple monthly return.

This assessment is consistent with the procedure in the script `src/04_markowitz_simulation.py`: the weights of the minimum-variance portfolio and of the maximum Sharpe Ratio portfolio are those identified exclusively on the training set and are kept unchanged during the test month. Therefore, the evaluation does not represent a new ex post optimization, but an out-of-sample application of the allocation decisions obtained previously.

From a methodological perspective, the expected simple monthly return derives from the annualized expected return estimated in the training sample. After calculating the daily logarithmic returns of the securities, their mean was annualized by multiplying it by 252 trading days. The portfolio's expected return was then obtained as the weighted average of the expected returns of the individual securities, using the weights estimated for each portfolio. Since the test period includes 14 trading days, the annualized expected return was scaled to the length of the test and converted into a simple return.

The realized simple monthly return, instead, was calculated using the returns actually observed during the test period. In particular, daily logarithmic returns were summed over the period considered, exploiting their additivity over time, and subsequently converted into a simple return. Finally, the realized portfolio return was obtained by combining the realized returns of the individual securities with the weights estimated in the training sample. In this way, the comparison between expected return and realized return makes it possible to assess the ability of portfolios constructed on historical data to produce consistent results out of sample.

More precisely, for each portfolio the script first calculates the expected average daily logarithmic return as the product of the weight vector and the mean logarithmic returns of the training set. This value is multiplied by the actual number of trading days in the test and then transformed into a simple return through \(\exp(r)-1\). The realized return follows the same conversion logic: the daily logarithmic returns of the portfolio in the test are summed and then converted into a simple return. The forecast error is finally defined as the difference between realized simple return and expected simple return.

The out-of-sample assessment table compares, for each portfolio, the return predicted on the basis of the training-set estimates with the return actually realized during the test period. The forecast error measures the difference between the realized result and the expected result: negative values indicate underperformance relative to the forecast, while the number of test days clarifies the effective time horizon of the comparison.

| Portfolio | Expected simple monthly return | Realized simple monthly return | Forecast error | Test days |
|-------------|------------------------------------|----------------------------------------|----------------------|----------------|
| Minimum variance | 0.6341% | 0.4448% | -0.1892% | 14 |
| Maximum Sharpe | 0.8350% | -0.2115% | -1.0466% | 14 |

The minimum-variance portfolio realized a monthly return slightly lower than expected, but relatively close to the forecast formulated on the basis of the training sample. The forecast error, equal to -0.1892%, indicates a limited deviation and confirms greater stability of the more conservative allocation during the month excluded from estimation. The maximum Sharpe Ratio portfolio, instead, underperformed more substantially relative to the expected monthly return and produced a negative realized return, equal to -0.2115%. This result highlights that in-sample optimality does not necessarily guarantee favorable out-of-sample performance: a portfolio constructed to maximize the return-risk ratio on historical data may be more exposed to market changes not present or not fully represented in the estimation period.

# 8. Conclusions

The project aimed to apply the Markowitz mean-variance model to a set of six U.S. stocks belonging to different sectors, in order to empirically evaluate the relationship between expected return and risk and to identify efficient portfolio allocations. The analysis combined a descriptive phase, intended to examine the statistical characteristics of returns, with an optimization phase, aimed at constructing the minimum-variance portfolio and the maximum Sharpe Ratio portfolio. In this sense, the study showed that portfolio selection cannot be based exclusively on the historical performance of individual securities, but must jointly consider volatility, correlations, and the marginal contribution of each asset to overall risk.

The main empirical results reveal significant heterogeneity among the analyzed securities. Exxon Mobil, JPMorgan Chase, and Apple have relatively higher historical average returns, while Coca-Cola and Johnson & Johnson show lower volatility and a more defensive profile. Boeing, by contrast, combines a negative average return with high volatility, making it less attractive within mean-variance optimization. The correlation matrix also indicates positive but generally moderate relationships among returns, confirming the existence of potential benefits from sectoral diversification. The p-values of the correlations confirm that these relationships are largely statistically significant; at the same time, the JNJ--BA case shows that a correlation can be statistically significant but economically weak.

Diversification emerges as a central element of the entire analysis. Risk reduction depends not only on the inclusion of less volatile securities, but also on the possibility of combining assets whose returns do not move in perfect synchrony. Investment in individual stocks exposes the investor to higher specific risk, linked to the operating, sectoral, and financial conditions of the individual firm. By contrast, a diversified portfolio makes it possible to attenuate these idiosyncratic components by distributing exposure across multiple sources of return and reducing dependence on the performance of a single security.

The Markowitz model proves useful because it provides a rigorous procedure for transforming historical information on returns, variances, and covariances into coherent allocation decisions. It makes it possible to identify efficient portfolios and to distinguish dominated combinations from those that offer the best trade-off between expected return and volatility. In particular, the minimum-variance portfolio should be interpreted as the most conservative allocation among feasible portfolios, because it minimizes overall volatility by assigning greater weights to the more stable and defensive securities, especially Coca-Cola and Johnson & Johnson. The maximum Sharpe Ratio portfolio, instead, represents the most efficient allocation in terms of expected return per unit of total risk: it accepts higher volatility than the minimum-variance portfolio, but obtains better compensation for risk through greater exposure to securities with higher historical returns, particularly Exxon Mobil, Apple, and JPMorgan Chase.

The out-of-sample assessment over the last month excluded from estimation provides a more realistic evaluation of the ability of portfolios to translate into actual performance. During that period, the minimum-variance portfolio showed greater stability than the maximum Sharpe Ratio portfolio, which recorded broader underperformance and a negative realized return. Overall, the comparison between investment in individual stocks and investment in a diversified portfolio confirms the value of portfolio construction. Although some individual securities may have higher average returns, they also involve specific risks that may be substantial. The portfolio approach instead makes it possible to evaluate each security not in isolation, but as a function of the contribution it provides to expected return and overall volatility. The efficient frontier summarizes this logic, showing that weight optimization can produce more balanced combinations than concentrated or random choices.

## Model limitations

Despite its analytical usefulness, the model has several important limitations. First, the analysis depends on the historical data used to estimate expected returns, volatility, and covariances. These quantities are not necessarily stable over time and may not reflect future market conditions. In particular, expected return estimates are often unstable and sensitive to the selected observation period, with possible significant effects on the optimal portfolio composition.

An additional limitation concerns the assumption of a constant covariance matrix. The model assumes that relationships among returns remain unchanged, whereas in reality correlations and volatility may change substantially during crises, macroeconomic changes, or sectoral shocks. In addition, the analysis excludes transaction costs, such as commissions, bid-ask spreads, and taxes, which in practice may reduce the attractiveness of certain reallocations. Finally, the constraint excluding short selling makes the problem more realistic for many investors, but limits the set of feasible strategies and prevents consideration of portfolios that might be efficient in the presence of negative positions.

## Possible future developments

Possible extensions of the analysis could include a larger number of financial assets, in order to improve the representativeness of the investable universe and evaluate broader diversification benefits. The inclusion of sector ETFs would also make it possible to compare investment in individual firms with instruments that are already diversified within specific economic sectors. A further development concerns the integration of international assets, which would be useful for analyzing the contribution of geographical diversification and exposure to markets characterized by different economic cycles, currencies, and risk structures.

From a theoretical perspective, the analysis could be extended by introducing the Capital Asset Pricing Model, in order to distinguish between total risk and systematic risk. This extension would make it possible to compare the overall volatility used in the Markowitz model with market beta, assessing the extent to which the risk of securities is diversifiable or instead attributable to common factors that cannot be eliminated through portfolio construction. In this way, the project could be expanded toward a more complete evaluation of the relationship among expected return, specific risk, and systematic risk.
