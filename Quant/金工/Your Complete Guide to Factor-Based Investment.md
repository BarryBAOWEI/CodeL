# 序言
序言由AQR的Cliff Asness撰写，序言讨论以下内容:
- 学术界和实业界提出了太多的因子，形成了John Cochrane所说的factor zoo
- 很多因子是通过数据挖掘产生的，危害性极大
- 然后对本书内容进行了梳理
    - 首先，虽然因子数量很多，但是很多因子属于同一主题
    - 本文提出了筛选因子的几大标准:persistence、pervasiveness、robustness、intuitiveness、investtability and information increasement
- 关于低波动和信用因子，Asness不赞同本书的讨论
- 本书的附录也很精彩
- 写这本书比写《巴菲特选股指南》更难，本书学术性和应用性都较强

# introduction
introduction中，介绍了以下内容：
- 因子的定义：factors are those specifical characteristics of stocks and securies that both explain performance and provid preminums.thus, a factor is a quantitative way of expressing a qualitative theme.
- Buffett的成功虽然可以归因于因子体系，但其先于学术界发现这些因子，这是其厉害之处
- 【论文】Yaron Levi, Ivo Welch.Long-Term Capital Budgeting.2014，检验了600多个因子
- 【论文】Campbell R.Harvey,Yan Liu and Heqing Zhu.and the Cross-Section of Expected Returns.2015,检验了315个因子，包括2010年~2012年发现的59个新因子

因子投资的视角：
- 资产之间相关性结构不稳定，相关性大（尤其是极端情况下），是以资产类别为视角的一个难题
- 【论文】Niels Pedersen etc.Asset Allocation: Risk Models for Alternative Investments.2014，发现私募股权和对冲基金分别与股票的相关性高达0.71和0.79
- 【论文】Clifford Asness etc.Do Hedge Funds Hedge?Be Cautions in Analyzing Monthly Returns.2001，和上面的结论一样，对冲基金可能大部分还是股票多头
- 其他另类资产中，REITs和基础设施等，也和股票市场相关性较高，商品和林地相对较低
- 【论文】Antti Ilmanen,Jared Kizer。The Death of Diversification has Been Greately Exaggerated.2012，提出从因子的视角进行配置，能有效减少组合波动

应该考虑哪些因子，标准如下：
- persistence，持久性，即因子有效性长期存在，即使被公开发表
- pervasiveness，普适性，在不同的证券类别和国家广泛存在
- robustness，稳健性，定义可以多样化，对参数不敏感
- intuitiveness，自觉性，即要有合理的逻辑，无论是从风险视角，还是行为金融视角
- investtability，可投资性，收益不能只停留在论文里，操作不能复杂，交易成本可控
- information increasement，差异性，即必须要有信息增量，不能被已有的其他因子解释

# chapter1：Market Beta
- CAPM在Harry Markowitz研究的的基础上，由John Lintner，William Sharpe和jack  Treynor三个人在1960s独立提出
- 市场beta的定义：Market beta expresses the degree to which an asset tends to move with the broad market. It is defined mathematically as the correlation between the asset's return and the market's return,multiplied by the ratio of the asset's volatility to the market's volatility.
- 在讲述market beta的持续性时，讲了几个硬道理：
    - 持有时间越长，胜率越高
    - 不过就算是持有20年，也不能保证胜率100%，这是需要投资者承担的风险
    - 投资成功的关键是忍耐和等待，就像巴菲特说的一样：the most import quality for an investor is temperament,not intellect
    - 对于投资这件事情来说，10年都不算长期，大多数人都在低点出来，高点进去
- 【论文】Dimson etc.Equity Premiums Around the Word.2016.测试了多个国家市场溢价，说明了market beta溢价具有普适性
- 交易费用和冲击成本较低，从指数基金和指数表现接近就能看出来
- 为什么market beta存在，可以从以下角度进行解释：
    - 股票市场和经济周期相关，当经济萧条时，收入降低甚至失业，同时股票资产也贬值，祸不单行。因此权益风险溢价是对承担“祸不单行”风险的补偿。
    - 股票大多数是有高净值人群持有，随着财富的提升，财富带来的边际效用逐渐递减，也没有更多的动力去承担更大的风险，除非风险补偿特别大
    - 从投资者生命周期的角度，年轻人愿意冒风险，喜欢投资股票，但收入低消费高，限制了他们参与股票市场；老年人，需要稳定的现金流，组合中股票数量逐渐降低；中年人是股票投资者的主力，他们收入稳定，但上有老小有小，不仅要为退休生活储蓄，还要为小孩的教育操心，比年轻人更厌恶风险，较高的权益风险溢价是对他们的补偿。
    - 从股票价格本身波动的角度，其年化波动20%左右，是国债的好几倍；另外，持有股票回撤会很大。因此，较大的风险带来较大的风险补偿
- 资产配置（因子配置）就像做菜一样，不仅要看单个食材的好坏，也要关注食材之间相互的配合和影响
- CAPM是有缺陷的，它不能解释组合所有收益来源；其他解释包括运气和能力(因子或择时)
- 【论文】Rolf Banz.The Relationship between Return and Market Value of Common Stocks.1981.发现市场贝塔并不能解释小盘股的较高收益
- 【论文】Sanjoy Basu.The Relationship between Earnings' Yield,Market Value and Return.1983.发现EP和和股票之间的正相关，不能被市场beta解释
- 【论文】BarrRosenberg etc.Persuasive Evidence of Market Inefficiency.1985.发现BM和股票收益有正向关系
- 【论文】Eugene Fama,Kenneth French.The Cross-Secction of Expected Stock Returns.1992.对市场beta、市值和价值因子进行总结，并提出Fama-French三因子模型

# chapter2：Size
- size factor定义（smb）：the size factor is calculated by taking the annual average return of small-cap stocks and subtracting the annual average return of large-cap stocks.
- 从risk-based角度进行解释，小盘股具有以下风险：
    - 较大的杠杆、融资更难、盈利的波动性、现金流的不确定、流动性差和公司治理不健全
    - 从股价本身来看，小盘股价格波动率更剧烈，回撤更大
    - 对货币政策较为敏感，扩张的货币政策有利于小盘股，紧缩时相反；对经济周期也比较敏感，在经济复苏时，小公司增长较快，经济萧条时，冲击也最大。【论文】不列
    - 小盘股里面，有一个坑，即small-cap growth异象，这些股票收益低波动大，尤其是那些盈利差，又过度对外投资的公司，需要规避
- 从行为金融的角度，可以有以下解释：
    - 【论文】Nicholas Barberis etc.Stocks as Lotteries：....2008.发现，投资者偏爱具有彩票效应的股票
    - 具有彩票效应的股票，收益具有正偏度，即可能有机会获得高收益。由于投资者的追捧，这类股票被“overpriced”，导致其未来负的超额收益
    - 具有彩票效应的股票包括：小盘股、次新股、私募股权、超低价股和困境股票
    - 既然彩票效应股票被高估，为什么聪明的投资不卖空已获得较高的超额收益呢？首先，许多机构投资者不允许卖空；其次，卖空成本不低，而且可卖空的股票有限，尤其是小的成长股；然后，根据前景理论，投资者也不愿意承担卖空可能带来的较大损失（对应彩票的较大收益）；最后，在还没盈利之前，借的股票就到期了，或者由于浮亏止损了
- 小盘股稳健吗？规模因子，既是一个阿尔法因子，也是一个风险因子。通过和其他因子结合，可以提高规模因子的稳健性。
    - 和大市值股票相比，动量因子和价值因子在小市值股票中表现更优
    - 【论文】Clifford Asness etc.Size Matters,If Yor Control Your Junk.2015.在控制了公司的质量因子后，小盘股的表现大幅提升，更稳定、更稳健、更持续、更纯粹、流动性更好
    - 另外，在控制beta因子后（即剔除高波动股票）后，也能提升size因子的表现
- 如何定义黑名单，这里又给出了一些想法：小盘成长股，高波动股，低流动股，junk股

# chapter3：Value
- value factor定义（hml）:taking the anunual average return of value stocks and substracting the annual average return of growth stocks.学术上一般用BtM（BP）定义价值股（top30%）和成长股（bottom30%）
- 从风险的角度进行解释：
    - 【论文】nai-fu Chen etc.Risk and Return of Value Stocks.1998.价值股票之所以便宜，是因为它们往往陷入在困境中，杠杆高，面临较多的盈利风险，因此价值股能获得更多的风险补偿
    - 【论文】Lu Zhang.The Value Premium.2005.价值股在经济扩张和萧条时，具有不对称的风险特征。在经济较差时，，价值股比成长股风险大得多；而在经济较好时，价值股只是稍微风险小点
    - 【论文】Robert F.Peterkort etc. Is the Book-to-Market Ratio a Measure of Risk.2005.这篇论文认为，BtM效应本质上是因为承担了杠杆风险。
    - Mohanmmed Elgammal etc.Value Premium and Default Risk.2014.价值溢价和违约风险有正相关
    - 【论文】AngelaJ.Black.The Value Premium and Economic Activity: Long-Run Evidence from the United States.研究了价值溢价和常见宏观变量之间的关系，包括工业产值（萧条或复苏）、货币供给（通胀或紧缩）和利率水平等，文章认为，价值溢价的存在是因为承担了过多的宏观风险。
    - 最后，从价值股价格波动来看，其波动率更大
- 从行为金融的角度进行解释：
    - 【论文】Josef Lakonishok etc.Contrarian Investment,Extrapolation and Risk.1994.对成长股太乐观，对价值股太悲观，导致前者被高估，后者被低估，直到估值修复；另一个解释是，投资者更容易接近成长股，也更熟悉成长股，导致其容易被高估
    - 【论文】Piotroski etc.Identifying Expectation Errors in Value/Glamours Strategies:A Fundamental Analysis Approach.2010.投资者具有选择性误差，成长股的投资者会忽略掉那些不利的信息，并找各种有利的信息来证明自己，因此对成长股过于乐观
    - 【论文】keith Anderson etc.Glamour,Value and Anchoring on the Changing P/E.2016.成长股投资者追求高PE股票，以此为锚点期望其越来越高，忽略了PE未来具有均值回归的特征
- 【论文】Brandes Institute.Value vs. Glamour: A Long-Term Worldwide Perspective.最后，用各种方式定义的价值因子，例如BP、EP和CFP，效果都很好

# chapter4：Momentum
- momentum定义（umd）: we define momentum as the last 12 months of returns excluding the most recent month(months 2-12).The most recent month is exclueded as it tends to show a reversal.the momentum factor is the average return of the top 30 percent of stocks minus the average return of the bottom 30 percent as ranked by this measure.
- 提出动量效应的的自两篇重要论文
    - 【论文】Narasimhan Jegadeesh and DSheridan Titman.Returns to Buying Winers and Selling Losers:Implications for Stock Market Efficiency.1993.是公认最初提出动量效应的文章了
    - 【论文】Mark Carhart.On Persistence in Mutual Fund Performance.1997.将动量因子和Fama-French三因子结合，提出解释基金收益的四因素模型
- 横截面动量VS时间序列动量
    - 横截面动量衡量的是相对表现，即在某一个时点上，做多相对表现较好的一篮子股票，做空相对表现较差的一篮子股票。因此，即使所有股票都在上涨，空头组合也会存在
    - 时间序列动量衡量的是绝对表现，即某一个时点上的价格和历史价格比较，自己和自己比。当所有股票都上涨的时候，就不存在空头了。
    - 本章指的是横截面动量
- 动量效应在多个资产和国家（地区）普遍存在，具体可以参考以下论文;
    - 【论文Tobias Moskowitz.Explanations for the Momentum Premium.2010.在40个国家和12个资产中，动量效应都存在
    - 【论文Clifford Asness etc.Value and Momentum Everywhere.2013.动量和价值效应不同市场和资产中普遍存在且统计显著，这些资产和市场包括个股（美国、英国、欧洲大陆和日本）、股票指数、政府债券、货币和商品
    - 【论文Eugene Fame and Kenneth French.Size,Value,and Momentum in International Stock Returns.2012.两位大佬检验了23个国际股票市场，从1989到2011年的因子效，发现除了日本动量效应都很显著。在【论文】Clifford Asness.Momentum in Japan：The Exception That Proves the Rule.2011中，价值因子在日本市场表现异常好，而价值和动量往往负相关，可能虚弱了动量因子的表现
    - 【论文】Christopher C.Geczy etc.215 Years of Global Multi-Asset Momentum:1800-2014(Equities,Sectors,Currencies, Bonds,Commodities and Stocks).2015.这是迄今为止时间跨度最长的动量因子回测，检验了47个国家指数、48个货币、43个政府债券、76个商品指数、301个全球行业以及34795个股票。他们发现，在这215年里动量效应在这6个资产中持续存在。
- 对动量效应的几个误解和解释
    - 动量因子，换手率往往偏大，是否会带来过多的成本，不利于策略执行呢？  【论文】Andrea Frazzini etc.Trading Costs of Asset Pricing Anomalies.研究了各类因子的执行成本，比得出以下结论：
        - 现在的交易成本比以前已经低多了
        - 通过使用算法交易，可以大大减少冲击成本，提高容量
        - 通过和其他低换手率低相关性的因子结合（例如动量和价值），也能显著减少换手率
    - 动量效应大部分来自空头，而不是多头。事实上不是这样子的。【论文】Clifford Asness etc.Fact,Fiction and Momentum Investing.2014. 动量因子在多头和空头都存在，而且比较均衡；即使难以获得空头收益，也能通过降低空头股票的权重间接做空空头。
    - 动量效应在小盘股中效果更好，是不是意味着不可执行？【论文】Robert Novy-Marx etc.A Taxonomy of Anomalies and Their Trading Costs.2016.研究了不同策略的换手率及交易成本，以及降低交易成本的三种策略。最后认为，设计优秀的动量策略对交易成本并没那么敏感
- 对动量效应的解释，从risk-based的角度较少，主要集中在行为金融的角度：
    - 【论文】Tobias Moskowitz【论文】Explanations for the Momentum Premium.这篇文章指出，投资者对信息短期内反应不足（underreaction），是导致动量效应的原因
    - 【论文】Zhi Da etc.Frog in the Pan:Continuous Information and Momentum.2014.提出了limiteed attention bias（有限注意力偏差），就像温水煮青蛙一样，投资者对一系列慢慢发布的、小的消息，反应较为迟钝，这造就了持续上涨和下跌的空间
    - 【论文】Markus Baltzer etc.Who Trades on Momentum.2015.另外一个行为解释是disposition effect（处置效应），即投资者为了避免后悔，会倾向继续持有已经浮亏的股票，而去变现浮盈的股票，这就导致定价错误，即低估winners和高估losers。理性的投资者（如机构投资者）看到了这个机会，会尝试从中获利，即买入winner卖出loser；由于机构投资者的套利限制，价格修正会很缓慢，就形成了我们看到的动量效应
- 从risk-based的角度进行解释：
    - 股票在经过一轮上涨之后，股票风险会增加
    - 流动性风险也能解释一部分
    - crash的存在

- 绕不过的crash：
    - 动量因子呈现尖峰肥尾左偏，即可能遭受大幅损失的风险。这种风险主要来自于空头端的反转。例如在2009年3月，动量最差的股票（空头端）表现反而最好，虽然多头也在挣钱，但long/short整体大幅亏钱；而long-only投资者不受此影响
    - 解决动量crash的方法有：
        - 【论文】Pedro Barroso etc.Momentum Has Its Moments.2015.通过目标波动模型进行风险管理，减少crash的影响...核对
        - 【论文】Denis B.Chaves.Idiosyncratic Momentum：US and International Evidence.2016.通过重新定义动量因子来减少crash的风险
        - 和其他因子结合，进行分散
        
# chapter5：The Profitability & Quatlity Factors
-  profitability定义（RMW）:the profitability factor is calculated by taking the annual average return of the top 30 percent of firms with high profitability minus the returns of the bottom 30 percent of firms whth low profitability.

- profitability最初的主要贡献：
    - 【论文】Robert Novy-Marx.the Other Side of Value:The Gross Profitability Premium.2013
    - 【论文】Eugene Fame and Kenneth French.Profitability,Investment and Average Return.2006
    - 【论文】Ral Ball etc.Accruals,Cash Flow,and Operation Profitability in the Cross Section of Stocks Returns.2016.剔除应计利润后的净利润，更纯粹
- 盈利因子广泛存在，从下面的研究就能看出
    - 【论文】Dimensional Fund.Dimensions of Equity Returns in Europe.2015.研究了欧洲15个国家33年的数据，发现盈利效应在欧洲绝大多数市场都存在
    - Masha Gordon.The Profitability Premuum in EM Markets.2013.研究了多个盈利因子（ROE、ROIC和营业利润）在新兴市场的表现，盈利因子溢价在新兴市场也是普遍存在的

- 从风险的角度进行解释
    - 盈利能力强的公司更多的是成长股，未来现金流具有不确定
    - 盈利能力强会吸引更多的竞争者，也会引起未来的不确定性

- 从直觉上来说，盈利能力强的公司应对财务困境的能力更强，风险更小，从风险的角度进行的解释，有点过于牵强。所以一般从行为金融的角度进行解释：
    - 【论文】Ryan Liu.Profitability Premium:Risk or Mispricing?2015.发现盈利公司在经济萧条的时候反而表现更好，并不具有更大风险，因此很难从risk的角度进行解释。从行为金融的角度，他们发现投资者对低盈利的的公司往往过度乐观，预期较高，也愿意在这类公司上赌一把，导致估值过高。由于套利限制，过度估值很难快速被消除。
    - 【论文】Jean-Philippe Bouchaud etc.The Excess Returns of "Quality" Stocks:A Behavioral Anomaly.2016.得出了相似的结论，即分析师群体往往过于乐观，但这种乐观在不同盈利能力股票中的程度不一样；盈利能力越强，乐观越弱；quality异象的存在就是由于显著低估好质量股票价格所致
    - 【论文】F.Y Eric C.Lam etc.The Profitability Premium:Macroeconomic Risks or Expectation Errors?.2016.同时从风险和行为金融的角度进行了解释，前者主要是一些宏观经济风险，包括gdp、通胀、期限结构和违约风险，能解释盈利溢价的1/3左右；后者主要是期望误差（expectation error），能解释剩余部分。
    - 【论文】HuiJun Wang etc.Dissecting the Profitabitliy Premium.2013.投资者没有对公司盈利的消息及时反应，因此高盈利的公司相对被低估，低盈利的公司相对被高估；由于套利的限制，阻碍了错误定价的修正。
- 不同的盈利指标，效果都很显著：
    - 如AQR用total profit-to-asset,total profits-to-sales,free cahs flow-to-assets计算profitability得分
    - Kewei Hou.Digesting Anomalies:An Investing Apporoch.2014.提出了一个新的四因子模型，即q-factor模型，包括market beta,size,investment和profitability，和FF提出的四因素模型极其相似
- 和质量（quality，qmj）因子关系
    - profitability是quality的一部分，quality包含了公司基本的其他方面
    - 高质量公司一般具有以下特征：low earnings volatility,high margins,high asset turnover(indicating efficent use of assets),low financial leverage,low operating leverage(indicating a strong balance sheet and low macroeconomic risk),and low stock-specific risk(volatility that is unexplained by macroeconomic activity)
    - 高质量公司在股市表现不好的时候，能够提供更高的收益，是一个很好的回撤保护器
- 解释buffet的阿尔法
    - 【论文】Andrea Frazzini etc.Buffett's Alpha.2013.除了应用来自伯克希尔成本较低的杠杆资金之外，巴菲特倾向于买安全边际高、便宜、高质量和大市值的股票
    - 【论文】Frazzini etc.Betting Against Beta.2014.发现如果考虑到市场beta，size，value，momentum，BAB，quality，和杠杆等因子，巴菲特的绝大部分收益都能被解释
    - 巴菲特在1994年股东大会上的名言：Ben Graham taguth me 45 years ago that in investing it is not necessary to do extraordinary things to get extraordinary results

# chapter6：The Term Factor
- 和股票一样，学术界也提出了两个因子用来解释债券组合收益，即term risk(duration)和default risk(credit)
- TERM定义：annual average return on long-term(20-year) U.S. government bonds minus the annual average return on one-month U.S. Treasury bills
- 基于风险的解释：
    - 对不可预期（unexpected inflation）的通货膨胀的补偿
    - 期限越长，债券波动越大

# appendix e: The Defualt Factor
- 需要说明的是，本书并不认为违约因子满足所有选择标准，所以把信用因子放在了附录。Asness是不同意这个结果的，越来越多的精细化研究也证明了default因子是一个十分有效的风格因子。
- DEF的定义：the return on long-term investment-grade bonds(20-year) minus the return on long-term government bonds(also 20-year)
- 本书认为，DEF溢价低，成本高，分散能力有限，性价比不行
- 【论文】Edwin J.Elton.Explaining the Rate Spread on Corporate Bonds.2001.公司债和股票都是公司发行的，都承担经环境变差的风险；信用风险绝大多数都能被权益风险模型解释，而且评级越低，解释力越强。因此信用风险带来的分散能力有限。
- 【论文】Martin Fridson.Do.High-Yield Bonds Have an Equity Component?1994.一个公司债可以理解为一个纯利率债加上卖空看跌期权。如果发行人的净资产低于了其负债，那么看跌期权就会被触发。对于高评级债，看跌期权极度虚值，期权费也低；对于高收益债券，违约容易发生，期权费较高。
- 【论文】Attakrit Asvanunt etc.The Credit Risk Premium.2016.重新审视了信用风险溢价。常用的计算credit premium的方式（A-B）不恰当，两者期限一样但久期并不一致，公司债较高的收益拥有更短的久期，因此低估了信用风险溢价。通过调整计算方式，发现信用风险溢价持续存在，且非常显著。另外，他们也发现了信用风险和权益风险有一定的正相关（相关性0.3）。
- 【论文】Jennie Bai.On Bounding Credit-Event Risk Premia.2015.这篇可以得出以下推论，除了短期公司债券外，其他公司债都面临权益风险。投资高收益债券和长期投资级债券，本质上是投资利率债和权益的混合。
- 为什么高收益债比投资级债券更有分散作用（相对于股票和利率债）：
    - 低评级的高收益债使得它们久期更短，因此对利率敏感度更低
    - 高收益债更容易被回售，有效久期更低
    - 低评级债券评级更容易被调高
    - 对公司股票价格的变化更敏感
- 【论文】Naresh Bansal etc.Equity Volatility as a Determinant of Future Term-Structure Volatility.2015.研究了利率债和股票如何相互作用。他们发现权益风险能够帮助我们预测期限风险，尤其是在股票波动率变大后两者相关性甚至为负。也就是说，在股市大跌期间（波动率变大），利率债能起到很好的缓冲作用，是不错的回撤保护器。
- 投资者一般喜欢具有正偏度的资产，因为这些资产具有彩票效益；相反，具有负偏度的资产，并不受投资者偏爱，这也是人们买保险的原因。而高收益债收益分布呈负偏度和肥尾特征，这使得其并不具有吸引力。

# chapter7：The Carry Factor
- 定义: a simplified description of carry is the return an investor receives(net of financing) if an asset's price remains the same.
- 【论文】Ralph Koijen etc.Carry.2015.发现在多个资产类别中，通过买多高carry同时卖空低carry，能获得显著收益
- 对carry的解释
    - 从供给和需求的角度看，高利率货币是因为货币需求大于供给，低利率货币是因为供给大于需求。根据传统的经济理论，即uncovered interest parity，由于存在套利机会，两个货币之间的利率差会通过升值或贬值的方式消除。然而事实上并没有，这就是UIP puzzle
    - UIP异象可能是由于非盈利参与者的存在导致的，例如央行和跨国公司的利率对冲。
    - 另外，carry策略并非毫无风险，例如当出现危机的时候，资本外逃到利率更低的避险货币。所以carry策略的收益是对这一风险的补偿
    - 【论文】Victoria Atanasov etc.Foreign Currency Returns and Systematic Risks.2015.发现货币收益和股票市场的资金流动冲击有较大联系
    - 【论文】Martin Lettau etc.Conditional Risk Premia in Currency Markets and Other Asset Classes.2014.高收益货币和股市波动更紧密，尤其是股市下跌时
    - 【论文】Charlotte Christiansen etc.The Time-Varying Systematic Risk of Carry Trade Strategies.2011.虽然carry策略很成功，但是在权益上有较多暴露，并且在外汇市场波动大时具有均值回归特征；另外，在股市发生crash时，carry策略也可能会经历较大的损失（即crash）。
    - 【论文】Lucio Sarno etc.Properties of Foreign Exchange Risk Premiums.2012
    - 【论文】Hanno Lustig etc.Common Risk Factors in Currency Markets.2011.在全球股票市场波动较大时，高利率货币倾向于贬值。
    - 【论文】Lukas Menkhoff etc.Carry Trades and Global Foreign Exchange Volatility.2012.超过90的carry横截面收益可以被外汇波动解释。在高波动期间，低利率货币由于升值可以提供保险。因此这些具有避险功能的货币具有较低的风险溢价。
    - 在前面提到Koijen的文章Carry中，也发现单个资产的carry收益往往具有超额峰度（肥尾），并且在经济变坏时（萧条或者流动性枯竭）收益下降较多。

- Carry策略的应用
    - 【论文】Vineer Bhansali.Carry and Trend in Lots of Place.2015.研究了四个资产类别在5个国家中carry和trend的应用，时间跨度从1960到2014。结果显示，同时具有正carry和正趋势的组合，能够获得更高的风险调整后收益
    - 【论文】Andrew Clare etc.Carry and Trend Following Returns in the Foreign Exchange Market.2015.也研究了carry和trend的结合。他们的研究，涵盖了39个货币从1981到2012的数据
    - AQR在开发风格溢价基金的时发现，carry因子和其他因子具有相对较低的相关性
    - 【论文】Klaus. Is There a Credit Risk Anomaly in FX Markets?2016.研究了国家主权信用和货币收益之间的关系。发现买多主权信用最低的国家货币，卖空主权信用最高的货币，能获得显著为负的收益。随着信用风险的增加，组合收益逐渐降低。这个和一般的风险资产定价理论不符。因此，建议只在高主权信用的国家中应用carry策略，或者避免买多低信用国家的债券。

# Appendix D:The Low-Volatility Factor
- 最初的资本资产定价模型CAPM，存在的一个大问题就是预测收益和风险正相关。但是经验研究发现，两者之间的关系实际上比较平缓（flat）甚至为负。
- 过去50年里，相比aggressive的股票，具有防御性质的股票（defensive，即低波动低风险）反而获得了更高的收益和风险调整后收益
- 事实上，低波动异象在1970s就被发现了（Fischer Black(1972)），比size和value还早
- 对低波动异象的解释
    - 【论文】David Blitz etc.Explanations for the Volatility Effect:An Overview Based on the CAPM Assumptions.2014.提出了较多关于低波动异象的解释
        - CAPM假设卖空和加杠杆是没有任何限制的，并且没有任何摩擦成本（交易成本或税收）。这两个假设并不成立。由于卖空和杠杆限制，再加上摩擦成本，投资者如果想要追求更大的收益的话，就不得不选择高beta股票。对高贝塔股票的过多需求和对低贝塔的过低需求，就能解释为什么风险和收益的flat甚至负的关系了。
        - 缺乏卖空机制的市场，股票也容易被高估。
        - CAPM假设投资者是风险厌恶的，只关心收益和波动，然后最大化自己的效用。实际上投资者是会有偏好的，例如喜欢彩票性质的股票（正偏度和超额峰度），使得他们会非理性地选择高波动股票。
        - 投资者最大化财富的效用的假设也不合理，研究表明，投资者更关心相对财富水平，而不是绝对财富水平。这隐含了一个相对平缓的证券市场线，即收益并不随风险单调变化，最大的beta收益最低。
        - 投资经理收入等于base+bonus，为了获得更高的奖金以及名誉，投资经理有动机变得更加冒险，虽然他们的客户可能是风险厌恶的。
        - CAPM假设投资拥有足够的信息，以及能够理性地处理这些信息。事实上也不是这样。研究表明，无论是个人投资者还是机构投资者，容易过度自信，都倾向于关注热门股（firms that are in the news more或attention grabbing），这些热门股往往交易活跃，最近表现较好，波动较高，价格呗高估。
- 认为波动因子并没有那么有效的文献：
    - 【论文】Robert Novy-Marx.Understanding Defensive Equity.2016.
        - 按照波动或beta排序分成5组，最大的1组表现都是最差的，而另外4组并非完全单调，最小的1组表现也并不是最好的
        - 高波动股票或高beta股票倾向于small-cap,unprofitable,and growth firms，即aggressive股票
        - 控制了市值、盈利和价值后，低波动策略几乎失效；低波动股票倾向于大盘股、价值股和盈利股
        - 低波动策略的收益只有1/6来自于多头端，绝大部分来自有空头。
        - 在小盘股中应用低波动策略，效果很好，因为规避了高风险股票（==这个很重要，这个很重要，这个很重要==）
    - 【论文】Xi Li etc.The Limits to Arbitrage and the Low-Volatility Anomaly.2014.
        - 波动因子多空组合信息衰减较快，只存在于组合构建后一个月内，并且容易受到交易成本的限制
        - 当剔除掉低价股后，效果会大打折扣
        - 随着时间的流逝，低波动效应慢慢衰减
    - 【论文】Bradford Jordan.The Long and Short of the Vol Anomaly.2016
        - 高波动和高卖空利率（成本）股票均表现出较差的风险调整后收益；高波动且低卖空利率的股票具有显著阿尔法收益，而高波动且高卖空利率的股票却明显表现差劲
        - 在股市黑天鹅事件时期，如互联网泡沫和08年金融危机期间，高波动低卖空利率组合能减少回撤
        - 因此，高波动并不完全是一件坏事情
    - DFA等公司用卖空利率来筛选股票池。当某一股票卖空利率特别高时，DFA会把该只股票从买入名单中移除15天。因为他们发现，高借票利率的股票，尤其是在小盘股中，未来一段时间往往表现不好。
- 低波动策略和期限因子有关，在期限因子上暴露为正。不难理解，低beta或低波动的股票和债券有点相似，通常是大盘股，盈利和股息稳定，安全边际较高。几篇相关的论文包括：
    - 【论文】Ronnie Shah.Understanding Low Volatility Strategies:Minimum Variance.2011.发现从1973到2010，低beta策略在期限风险因子上的暴露显著为正
    - 【论文】Tzee-man etc.A Study of Low-Volatility Portfolio Construction Methods.2014.发现BAB因子和久期相关性为0.2
    - 【论文】David Blitz etc.Interest Rate Risk in Low-Volatility Strategies.2014.发现在债券上的暴露确实能解释低波动因子效应，但不能完全解释
-支持的声音也很多
    - 【论文】Andrea Frazzini etc.Betting Against Beta.2014
    - 【论文】David Blitz etc.The Volatility Effect:Lower Risk Without Lower Return.2007
    - 【论文】David Blitz etc.The Volatility Effect in Emerging Markets.2013
- 【论文】Pim van Vlie.Enhancing a Low Volatility Strategy is Particulary Helful When Generic Low Volatility is Expensive.2012.发现低波动策略在价值因子上会有暴露，但是这种暴露是时变的。

# Appendix F:Time-Series Momentum
- 需要说明的是，时间序列动量满足所有的标准，但是不是横截面的，所以放在了附录来介绍。
- 【论文】Ian D'Souza etc.The Enduring Effect of Time-Series Momentum on Stock Return over Nearly 100-years.2016.研究跨度从1927到2014共88年，结论基本满足评价因子是否有效的所有条件。文章也指出了可以用投资者反应不足解释趋势跟踪收益来源，包括gradual information diffusion model和frog in the pan model
- 【论文】Brian Hurst etc.A Century of Evidence on Trend-Following Investing.2014.文章定义了三个动量：1月动量、三月动量和12月动量，涉及4个资产类型共67个资产（包括29个商品、11个权益指数、15个债券指数和12个或币），时间横跨1880年1月到2013年12月。他们的研究指出，在各个资产类型和时间区间内，时间序列动量表现优秀，即使考虑“2-and-20”费率结构后仍然显著为正；另外，时间序列动量在股市大跌时异常有效，在历史上10次黑天鹅事件期间，有8次实现了正收益。AQR从行为金融的角度对该因子进行了解释，即锚点效应和羊群效应，以及中央银行等非盈利机构的存在
- Akindynos-Nikolaos Baltas etc.Momentum Strategies in Futures Markets and Trend-Following Funds.2013.利用1974到2012年共71个品种数据，研究了期货市场时间序列动量策略和cta基金的关系，也探讨了该策略的容量问题
- Mark C. Hutchinson etc. Is This Time Different?Trend Following and Financial Crises.2014.

# Chapter 8:Does Publication Reduce the Size of Premiums?
- 如果异象是行为偏差的结果，理论上聪明的投资人看到机会后迅速进行修正；但是由于套利限制（限制卖空或成本过高等），异象很难被消除；如果是异象是风险相关的原因，那么资金的流入肯定会减少溢价。话不多说，直接上论文。
- 【论文】Paul Calluzzo etc.Anomalies Are Publicized Broadly,Institutions Trade Accordingly,and Returns Decay Correspondingly.2015.机构投资者和学术论文发表，会使资产价格更加合理，市场更优效率
- 【论文】R.David etc.Does Academic Research Destroy Stock Return Predictability?2015.检查了97个因子中的85个后发现，学术研究发表后，确实能够引导资金流入使得溢价减少（平均减少32%），但不会消失
- 【论文】Heiko Jacobs etc.Anomalies Across the Globe:One Public,No Longer Existent?2016.这篇研究主要研究39个市场的138个异象，在1981到2013年学术公开前后的收益。和美国相比，这些异象在其他市场并没有因为学术发表而减弱，反而效果更好了。
- 接下来看看市值、价值和动量因子是否因为学术发表而减弱；之所以不讨论盈利、质量等，是因为这些异象比较新，近几年才被学术发现。市值、价值和动量都在论文公开后溢价变小，但没有消失，仍然值得关注和配置。
- 最后，介绍了为什么美国市场风险溢价会减少。包括流动性的改善，对投资者的保护，监管能力的提升，衍生工具的丰富以及套利交易的活跃等
- 另外两篇论文解释了为什么异象会持续
    - 【论文】Yongqing Chu etc.The Causal Effect of Limits to Arbitrage on Asset Pricing Anomalies.2016.由于卖空限制、卖空成本较高、卖空潜在亏损较大以及税收等因素，使得错误定价持续存在
    - 【论文】Malcolm Baker etc.Benchmark as Limits to Arbitrage:Understanding the Low-Volatility Anomaly.2011.本篇论文从另外一个角度进行了分析。因为机构投资者会有一个比较基准，偏离业绩基准会影响基金经理的业绩，这限制了他们追求异象溢价
- 总结，学术研究的公布，会吸引对冲基金等聪明的投资者进入，使得溢价减少，大约减少1/3；卖空限制等因素，会使得异象长期存在

# Chapter 9：Implementing A Diversified Factor Portfolio
- 这章主要讲多个因子分散的好处，提到两篇论文;
    - 【论文】Erik Hjalmarsson.Portfolio Diversification Across Characteristics.2011
    - 【论文】Larry Swedroe etc.Reducing the Risk of Black Swans:Using the Science of Investing to Capture Returns with Less Volatility.

# Appendix A：Tracking error regret:the investor's enemy
- 分散投资的好处就不说了，但分散会面临一个风险：tracking error regret，即我们的分散组合跑输了一个常见的比较基准，如标普500指数
- 例如，如果从08年初到15年（包括08年的金融危机），美国股市表现非常好，而国际市场却很糟糕；但是如果站在08年初，从00年到08年，国际市场远远好于美国市场。如果站在08年初，（美国）投资者肯定认为分散（投资于国际股票）有肉吃，但是最近10年来看，相比于美国市场（benchmark），分散明显少赚很多。这就会带来traking error regret
- 之所以会有这种后悔，主要来自于两个人性的弱点：relativism和recency
    - relativism，即相对主义或锚点效应，即投资者喜欢比较，和身边的朋友比较，很一个选择的benchmark比较
    - recency,即代表性偏差，最近的事情会影响投资者的判断，使得他们容易追涨杀跌
- 投资需要耐心，一般人认为3年5年就是长期，10年就是一生；实际上，在投资领域，10年都算短期。在本世纪初的10年，标普500年化收益-1%；在09年前的40年，美国大盘股和小盘股都没有跑赢长期国债....

# Appendix B:The Truth Abount Smart beta
- 多因子（multi-style）比单因子（single-style）能带来成本上减少，例如同时投资动量风格基金和价值风格基金时，股票A由于价格降低动量减少从而被移除动量基金，但落入了价值风格基金的股票池，从而又被买入。而多因子模型，会综合考虑两个因子，会减少换手带来的成本
- 基金之间的差别，可能的因素有很多，包括因子的定义和暴露，组合构建过程（池子，黑名单，权重，因子暴露），交易执行（建仓时点，冲击成本），再平衡（频率，方式），风险管理（尾部风险）等

# Appendix G:Marginal Utility of incremental factors on fund return
-【论文】FF.Incremental Variables and the Investment Opportunity Set.2015.认为一个因子能带来增量信息才有意义
-【论文】Roger Clarke.Factor Portfolios and Efficient Factor Investing.2016.认为，多因子模型由于多个单独因子。例如价值和市值，如果单独持有小市值股票，可能会有很多成长股；如果单独持有价值股，会有很多大盘股。两者结合，才能做到相对最优，同时成本也能降低

# Appendix I:Reevaluating the size premium
- 在fama-french三因子模型中，定义size因子为，按照NYSE股票市值分成10组，最小的5组加权平均-最大的5组加权平均。而在定义其他因子时，包括价值、质量和动量等，都是30-30.如果改变size50-50的定义，例如30-30，或者20-20，size溢价能提升不少
 

# 附录
资本市场线VS证券市场线(来自知乎)
- 测度内容不一致
    - 资本市场线测度的是：由风险资产和无风险资产构成组合的期望收益与风险的关系
    - 证券市场线测度的是：市场均衡条件下单项或组合资产的期望收益与风险的关系

- 度量单位不一致
    - 资本市场线度量单位：标准差（Standard Deviation）
    - 证券市场线度量单位：β系数 （Beta coefficient）
- 适用情况不同
    - 资本市场线适用有效的资产组合
    - 证券市场线则单项资产或组合资产的情况均适用
