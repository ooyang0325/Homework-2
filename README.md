# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution
path: `tokenB` -> `tokenA` -> `tokenD` -> `tokenC` -> `tokenB `
tokenB balance:  `20.129888944077446732`
    1. `5` tokenB -> `5.655321988655321988` tokenA
    2. `5.655321988655321988` tokenA -> `2.458781317097933552` tokenD
    3. `2.458781317097933552` tokenD -> `5.088927293301515695` tokenC
    4. `5.088927293301515695` tokenC -> `20.129888944077446732` tokenB

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution
> slippage是指實際買入價格與預期買入價格的差異
```solidity
function swapTokensForExactTokens(
  uint amountOut,
  uint amountInMax,
  address[] calldata path,
  address to,
  uint deadline
) external returns (uint[] memory amounts);
```
> 此function當中的amountInMax限制了能夠付出的上限，避免slippage發生時交易繼續進行。

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution
> minimum liquidity可以避免有心人士創造規模太小的流動池，此類流動池容易形成數量差異過大的交易對並受人操控。

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution
> LP token = min(amount0 / _reserve0 * total_totalSupply, amount1 / _reserve1 * total_totalSupply)
> 這樣的公式確保了你投入流動池的token數量與你得到的份額(LP token)是相符的，但當你投入某一個token的比例多過於另一個token時，你所得到的份額會是較少的token的比例。

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution
> 攻擊者透過加高gas的方式，先在你交易執行前先買入你要買的token，使該token的價格提高，並在你實際買入之後，將先前購買的token以較高價賣出。
> 三明治攻擊會讓交易產生slippage，讓你交易失敗或獲利減少。

