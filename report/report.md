# 1. Introduction

Portfolio construction is a central problem in finance because investors rarely evaluate securities in isolation. Instead, they allocate capital across several assets in order to pursue an investment objective while controlling exposure to uncertainty. A well-constructed portfolio provides a systematic basis for deciding how much wealth should be assigned to each asset, rather than relying only on individual stock characteristics or informal judgement.

A fundamental issue in portfolio choice is the trade-off between risk and return. In general, investors require higher expected returns as compensation for accepting greater uncertainty in future outcomes. Riskier assets may offer the possibility of higher gains, but they also expose investors to larger potential losses and more volatile performance. Portfolio analysis therefore requires both an estimate of expected return and a measure of risk, so that alternative allocations can be compared consistently.

Diversification plays an important role in managing this trade-off. By combining assets whose returns do not move perfectly together, an investor may reduce total portfolio risk without necessarily reducing expected return by the same proportion. The benefit of diversification depends not only on the risk of each individual asset, but also on the covariance and correlation among asset returns. As a result, portfolio construction must consider the interaction between securities as well as their individual expected performance.

The objective of this project is to analyze six stocks from different sectors and build efficient portfolios using the Markowitz mean-variance model. The project applies portfolio theory to a diversified set of equities, estimates return and risk characteristics from historical data, and provides the theoretical foundation for identifying portfolios that offer efficient combinations of expected return and risk.

# 2. Theoretical Background

Risky investments are assets whose future returns are uncertain. Common stocks are risky because their prices and dividends may change in response to firm-specific developments, industry conditions, macroeconomic factors, interest rates, investor expectations, and broader market movements. Because the future payoff is not known with certainty, investors must evaluate both the expected reward from holding an asset and the variability of possible outcomes around that expectation.

The risk-return relationship is one of the basic principles of financial decision-making. Investors generally expect to receive higher returns for bearing higher levels of risk. However, higher risk does not guarantee higher realized returns; it only indicates greater uncertainty and a wider range of possible outcomes. For this reason, portfolio analysis distinguishes between expected return, which represents the anticipated average outcome, and risk, which is commonly measured by variance or standard deviation of returns.

Risk aversion describes the preference of most investors to avoid unnecessary risk. A risk-averse investor will choose the less risky of two investments if both offer the same expected return. Conversely, the investor will accept additional risk only if the expected return is sufficiently higher to compensate for that risk. This assumption is important in mean-variance analysis because it explains why investors seek portfolios that minimize risk for a given expected return or maximize expected return for a given level of risk.

Mean-variance analysis evaluates portfolios using two primary quantities: expected return and variance. The expected return represents the average return the investor anticipates from the portfolio, while variance measures the dispersion of returns around that expectation. In this framework, an investor compares portfolios according to their expected return and risk, assuming that these two dimensions provide a useful summary of investment performance.

Diversification is the process of allocating wealth across multiple assets rather than concentrating the entire investment in a single security. The purpose of diversification is to reduce exposure to asset-specific risk. When assets are not perfectly positively correlated, losses or weak performance in one asset may be partly offset by stronger performance in another. Therefore, the risk of a diversified portfolio depends on both individual asset volatilities and the relationships among asset returns.

The expected return of a portfolio is the weighted average of the expected returns of the assets included in the portfolio. If a portfolio contains \(n\) assets, where \(w_i\) is the weight assigned to asset \(i\) and \(E(R_i)\) is the expected return of asset \(i\), the expected portfolio return is:

$$
E(R_p) = \sum_{i=1}^{n} w_i E(R_i)
$$

Portfolio variance measures the risk of the combined portfolio. Unlike expected return, portfolio variance is not only a weighted average of individual asset variances. It also depends on covariances between asset returns. Covariance measures the extent to which two assets tend to move together. Positive covariance indicates that assets often move in the same direction, while negative covariance indicates that they often move in opposite directions. Lower covariance between assets increases the potential benefit from diversification.

Using matrix notation, portfolio variance can be written as:

$$
\sigma_p^2 = w^T \Sigma w
$$

where \(w\) is the vector of portfolio weights and \(\Sigma\) is the covariance matrix of asset returns. This expression shows that portfolio risk depends on the complete covariance structure of the assets, not only on the risk of each security separately.

In a fully invested portfolio, the portfolio weights must sum to one. This condition ensures that all available capital is allocated across the selected assets:

$$
\sum_{i=1}^{n} w_i = 1
$$

The efficient frontier is the set of portfolios that provide the highest expected return for each level of risk, or equivalently, the lowest risk for each level of expected return. Portfolios below the efficient frontier are inefficient because another feasible portfolio offers either a higher expected return for the same risk or a lower risk for the same expected return. The efficient frontier therefore provides a useful visual and analytical representation of the best attainable risk-return combinations within a given set of assets.

Markowitz portfolio theory, developed by Harry Markowitz, formalizes portfolio selection through the mean-variance framework. The theory emphasizes that investors should not select assets solely on the basis of individual expected returns or individual risks. Instead, they should evaluate how assets interact within a portfolio through covariance. By combining expected returns, variances, covariances, and portfolio weight constraints, the Markowitz model identifies efficient portfolios and provides a rigorous foundation for modern portfolio construction.
