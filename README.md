# Government bond auction demand across OECD countries

Downloads government bond and bill **auction results** from each OECD country's
official debt office or central bank (plus the European Union's own
auctions), then charts demand (bid-to-cover), volume, yields and, where the
central bank buys at auction, the central bank's share, over the last 20
years, broken down by maturity. It then looks for the months when yields
shifted to a new level and checks them against known events (see
[Analysis](#analysis-when-and-why-yields-shifted)).

For the **last 12 months** nothing is averaged: every single auction is shown
as a dot, next to the **daily market yield** for the same maturity wherever the
country publishes one, so moves between auctions show up too.

![10-year government bond yields: daily market vs every auction, last 12 months](results/auctions/global/global_10year_recent_yield_12m.png)

## Market yields, all countries

The daily yield on existing government bonds as they trade, for the 10
countries that publish it free (see [Daily market yields](#daily-market-yields-10-countries)).

![10-year government bond market yields, last 12 months](results/market_yields/global/global_10year_market_yields_12m.png)

<details>
<summary><b>Every maturity, by country</b> (click to open)</summary>

![Government bond market yields by maturity, last 12 months](results/market_yields/global/global_market_yields_grid_12m.png)

All the numbers: [global_market_yields_12m.csv](results/market_yields/global/global_market_yields_12m.csv)

</details>

## Results by country

Click a country to open its charts; click again to close it. Every chart and
data file is also in [`results/`](results/).

<!-- One <details> block per country, generated from results/ after each run. -->
<details>
<summary><b>United States</b> (daily market yields)</summary>

**Every auction vs the daily market yield, last 12 months**

![United States: Every auction vs the daily market yield, last 12 months](results/auctions/us/us_recent_yield_12m.png)

**Daily market yields by maturity, last 12 months**

![United States: Daily market yields by maturity, last 12 months](results/market_yields/us/us_market_yields_12m.png)

**Bid-to-cover at every auction, last 12 months**

![United States: Bid-to-cover at every auction, last 12 months](results/auctions/us/us_recent_bid_to_cover_12m.png)

**Auction yields, 20 years (3-month average)**

![United States: Auction yields, 20 years (3-month average)](results/auctions/us/us_auction_yield_20y.png)

**Bid-to-cover, 20 years (3-month average)**

![United States: Bid-to-cover, 20 years (3-month average)](results/auctions/us/us_bid_to_cover_20y.png)

More: [every auction, last 12 months (with the market yield that day)](results/auctions/us/us_recent_auctions_12m.csv) · [daily market yields, last 12 months](results/market_yields/us/us_market_yields_12m.csv) · [monthly data, 20 years](results/auctions/us/us_auction_20y_monthly.csv) · [volume chart](results/auctions/us/us_accepted_20y.png) · [central bank share chart](results/auctions/us/us_central_bank_share_20y.png) · [non-dealer share chart](results/auctions/us/us_nondealer_share_20y.png)

</details>

<details>
<summary><b>Canada</b> (daily market yields)</summary>

**Every auction vs the daily market yield, last 12 months**

![Canada: Every auction vs the daily market yield, last 12 months](results/auctions/canada/canada_recent_yield_12m.png)

**Daily market yields by maturity, last 12 months**

![Canada: Daily market yields by maturity, last 12 months](results/market_yields/canada/canada_market_yields_12m.png)

**Bid-to-cover at every auction, last 12 months**

![Canada: Bid-to-cover at every auction, last 12 months](results/auctions/canada/canada_recent_bid_to_cover_12m.png)

**Auction yields, 20 years (3-month average)**

![Canada: Auction yields, 20 years (3-month average)](results/auctions/canada/canada_auction_yield_20y.png)

**Bid-to-cover, 20 years (3-month average)**

![Canada: Bid-to-cover, 20 years (3-month average)](results/auctions/canada/canada_bid_to_cover_20y.png)

More: [every auction, last 12 months (with the market yield that day)](results/auctions/canada/canada_recent_auctions_12m.csv) · [daily market yields, last 12 months](results/market_yields/canada/canada_market_yields_12m.csv) · [monthly data, 20 years](results/auctions/canada/canada_auction_20y_monthly.csv) · [volume chart](results/auctions/canada/canada_accepted_20y.png) · [central bank share chart](results/auctions/canada/canada_central_bank_share_20y.png)

</details>

<details>
<summary><b>United Kingdom</b> (daily market yields)</summary>

**Every auction vs the daily market yield, last 12 months**

![United Kingdom: Every auction vs the daily market yield, last 12 months](results/auctions/uk/uk_recent_yield_12m.png)

**Daily market yields by maturity, last 12 months**

![United Kingdom: Daily market yields by maturity, last 12 months](results/market_yields/uk/uk_market_yields_12m.png)

**Bid-to-cover at every auction, last 12 months**

![United Kingdom: Bid-to-cover at every auction, last 12 months](results/auctions/uk/uk_recent_bid_to_cover_12m.png)

**Auction yields, 20 years (3-month average)**

![United Kingdom: Auction yields, 20 years (3-month average)](results/auctions/uk/uk_auction_yield_20y.png)

**Bid-to-cover, 20 years (3-month average)**

![United Kingdom: Bid-to-cover, 20 years (3-month average)](results/auctions/uk/uk_bid_to_cover_20y.png)

More: [every auction, last 12 months (with the market yield that day)](results/auctions/uk/uk_recent_auctions_12m.csv) · [daily market yields, last 12 months](results/market_yields/uk/uk_market_yields_12m.csv) · [monthly data, 20 years](results/auctions/uk/uk_auction_20y_monthly.csv) · [volume chart](results/auctions/uk/uk_accepted_20y.png)

</details>

<details>
<summary><b>Germany</b> (daily market yields)</summary>

**Every auction vs the daily market yield, last 12 months**

![Germany: Every auction vs the daily market yield, last 12 months](results/auctions/germany/germany_recent_yield_12m.png)

**Daily market yields by maturity, last 12 months**

![Germany: Daily market yields by maturity, last 12 months](results/market_yields/germany/germany_market_yields_12m.png)

**Bid-to-cover at every auction, last 12 months**

![Germany: Bid-to-cover at every auction, last 12 months](results/auctions/germany/germany_recent_bid_to_cover_12m.png)

**Auction yields, 20 years (3-month average)**

![Germany: Auction yields, 20 years (3-month average)](results/auctions/germany/germany_auction_yield_20y.png)

**Bid-to-cover, 20 years (3-month average)**

![Germany: Bid-to-cover, 20 years (3-month average)](results/auctions/germany/germany_bid_to_cover_20y.png)

More: [every auction, last 12 months (with the market yield that day)](results/auctions/germany/germany_recent_auctions_12m.csv) · [daily market yields, last 12 months](results/market_yields/germany/germany_market_yields_12m.csv) · [monthly data, 20 years](results/auctions/germany/germany_auction_20y_monthly.csv) · [volume chart](results/auctions/germany/germany_accepted_20y.png)

</details>

<details>
<summary><b>Japan</b> (daily market yields)</summary>

**Every auction vs the daily market yield, last 12 months**

![Japan: Every auction vs the daily market yield, last 12 months](results/auctions/japan/japan_recent_yield_12m.png)

**Daily market yields by maturity, last 12 months**

![Japan: Daily market yields by maturity, last 12 months](results/market_yields/japan/japan_market_yields_12m.png)

**Bid-to-cover at every auction, last 12 months**

![Japan: Bid-to-cover at every auction, last 12 months](results/auctions/japan/japan_recent_bid_to_cover_12m.png)

**Auction yields, 20 years (3-month average)**

![Japan: Auction yields, 20 years (3-month average)](results/auctions/japan/japan_auction_yield_20y.png)

**Bid-to-cover, 20 years (3-month average)**

![Japan: Bid-to-cover, 20 years (3-month average)](results/auctions/japan/japan_bid_to_cover_20y.png)

More: [every auction, last 12 months (with the market yield that day)](results/auctions/japan/japan_recent_auctions_12m.csv) · [daily market yields, last 12 months](results/market_yields/japan/japan_market_yields_12m.csv) · [monthly data, 20 years](results/auctions/japan/japan_auction_20y_monthly.csv) · [volume chart](results/auctions/japan/japan_accepted_20y.png)

</details>

<details>
<summary><b>Austria</b> (auctions only)</summary>

**Every auction vs the daily market yield, last 12 months**

![Austria: Every auction vs the daily market yield, last 12 months](results/auctions/austria/austria_recent_yield_12m.png)

**Auction yields, 20 years (3-month average)**

![Austria: Auction yields, 20 years (3-month average)](results/auctions/austria/austria_auction_yield_20y.png)

More: [every auction, last 12 months (with the market yield that day)](results/auctions/austria/austria_recent_auctions_12m.csv) · [monthly data, 20 years](results/auctions/austria/austria_auction_20y_monthly.csv) · [volume chart](results/auctions/austria/austria_accepted_20y.png)

</details>

<details>
<summary><b>Belgium</b> (daily market yields)</summary>

**Every auction vs the daily market yield, last 12 months**

![Belgium: Every auction vs the daily market yield, last 12 months](results/auctions/belgium/belgium_recent_yield_12m.png)

**Daily market yields by maturity, last 12 months**

![Belgium: Daily market yields by maturity, last 12 months](results/market_yields/belgium/belgium_market_yields_12m.png)

**Bid-to-cover at every auction, last 12 months**

![Belgium: Bid-to-cover at every auction, last 12 months](results/auctions/belgium/belgium_recent_bid_to_cover_12m.png)

**Auction yields, 20 years (3-month average)**

![Belgium: Auction yields, 20 years (3-month average)](results/auctions/belgium/belgium_auction_yield_20y.png)

**Bid-to-cover, 20 years (3-month average)**

![Belgium: Bid-to-cover, 20 years (3-month average)](results/auctions/belgium/belgium_bid_to_cover_20y.png)

More: [every auction, last 12 months (with the market yield that day)](results/auctions/belgium/belgium_recent_auctions_12m.csv) · [daily market yields, last 12 months](results/market_yields/belgium/belgium_market_yields_12m.csv) · [monthly data, 20 years](results/auctions/belgium/belgium_auction_20y_monthly.csv) · [volume chart](results/auctions/belgium/belgium_accepted_20y.png)

</details>

<details>
<summary><b>Czech Republic</b> (auctions only)</summary>

**Every auction vs the daily market yield, last 12 months**

![Czech Republic: Every auction vs the daily market yield, last 12 months](results/auctions/czechia/czechia_recent_yield_12m.png)

**Bid-to-cover at every auction, last 12 months**

![Czech Republic: Bid-to-cover at every auction, last 12 months](results/auctions/czechia/czechia_recent_bid_to_cover_12m.png)

**Auction yields, 20 years (3-month average)**

![Czech Republic: Auction yields, 20 years (3-month average)](results/auctions/czechia/czechia_auction_yield_20y.png)

**Bid-to-cover, 20 years (3-month average)**

![Czech Republic: Bid-to-cover, 20 years (3-month average)](results/auctions/czechia/czechia_bid_to_cover_20y.png)

More: [every auction, last 12 months (with the market yield that day)](results/auctions/czechia/czechia_recent_auctions_12m.csv) · [monthly data, 20 years](results/auctions/czechia/czechia_auction_20y_monthly.csv) · [volume chart](results/auctions/czechia/czechia_accepted_20y.png)

</details>

<details>
<summary><b>Denmark</b> (auctions only)</summary>

**Every auction vs the daily market yield, last 12 months**

![Denmark: Every auction vs the daily market yield, last 12 months](results/auctions/denmark/denmark_recent_yield_12m.png)

**Bid-to-cover at every auction, last 12 months**

![Denmark: Bid-to-cover at every auction, last 12 months](results/auctions/denmark/denmark_recent_bid_to_cover_12m.png)

**Auction yields, 20 years (3-month average)**

![Denmark: Auction yields, 20 years (3-month average)](results/auctions/denmark/denmark_auction_yield_20y.png)

**Bid-to-cover, 20 years (3-month average)**

![Denmark: Bid-to-cover, 20 years (3-month average)](results/auctions/denmark/denmark_bid_to_cover_20y.png)

More: [every auction, last 12 months (with the market yield that day)](results/auctions/denmark/denmark_recent_auctions_12m.csv) · [monthly data, 20 years](results/auctions/denmark/denmark_auction_20y_monthly.csv) · [volume chart](results/auctions/denmark/denmark_accepted_20y.png)

</details>

<details>
<summary><b>Finland</b> (auctions only)</summary>

**Every auction vs the daily market yield, last 12 months**

![Finland: Every auction vs the daily market yield, last 12 months](results/auctions/finland/finland_recent_yield_12m.png)

**Bid-to-cover at every auction, last 12 months**

![Finland: Bid-to-cover at every auction, last 12 months](results/auctions/finland/finland_recent_bid_to_cover_12m.png)

**Auction yields, 20 years (3-month average)**

![Finland: Auction yields, 20 years (3-month average)](results/auctions/finland/finland_auction_yield_20y.png)

**Bid-to-cover, 20 years (3-month average)**

![Finland: Bid-to-cover, 20 years (3-month average)](results/auctions/finland/finland_bid_to_cover_20y.png)

More: [every auction, last 12 months (with the market yield that day)](results/auctions/finland/finland_recent_auctions_12m.csv) · [monthly data, 20 years](results/auctions/finland/finland_auction_20y_monthly.csv) · [volume chart](results/auctions/finland/finland_accepted_20y.png)

</details>

<details>
<summary><b>France</b> (auctions only)</summary>

**Every auction vs the daily market yield, last 12 months**

![France: Every auction vs the daily market yield, last 12 months](results/auctions/france/france_recent_yield_12m.png)

**Bid-to-cover at every auction, last 12 months**

![France: Bid-to-cover at every auction, last 12 months](results/auctions/france/france_recent_bid_to_cover_12m.png)

**Auction yields, 20 years (3-month average)**

![France: Auction yields, 20 years (3-month average)](results/auctions/france/france_auction_yield_20y.png)

**Bid-to-cover, 20 years (3-month average)**

![France: Bid-to-cover, 20 years (3-month average)](results/auctions/france/france_bid_to_cover_20y.png)

More: [every auction, last 12 months (with the market yield that day)](results/auctions/france/france_recent_auctions_12m.csv) · [monthly data, 20 years](results/auctions/france/france_auction_20y_monthly.csv) · [volume chart](results/auctions/france/france_accepted_20y.png)

</details>

<details>
<summary><b>Greece</b> (auctions only)</summary>

**Every auction vs the daily market yield, last 12 months**

![Greece: Every auction vs the daily market yield, last 12 months](results/auctions/greece/greece_recent_yield_12m.png)

**Bid-to-cover at every auction, last 12 months**

![Greece: Bid-to-cover at every auction, last 12 months](results/auctions/greece/greece_recent_bid_to_cover_12m.png)

**Auction yields, 20 years (3-month average)**

![Greece: Auction yields, 20 years (3-month average)](results/auctions/greece/greece_auction_yield_20y.png)

**Bid-to-cover, 20 years (3-month average)**

![Greece: Bid-to-cover, 20 years (3-month average)](results/auctions/greece/greece_bid_to_cover_20y.png)

More: [every auction, last 12 months (with the market yield that day)](results/auctions/greece/greece_recent_auctions_12m.csv) · [monthly data, 20 years](results/auctions/greece/greece_auction_20y_monthly.csv) · [volume chart](results/auctions/greece/greece_accepted_20y.png)

</details>

<details>
<summary><b>Hungary</b> (daily market yields)</summary>

**Every auction vs the daily market yield, last 12 months**

![Hungary: Every auction vs the daily market yield, last 12 months](results/auctions/hungary/hungary_recent_yield_12m.png)

**Daily market yields by maturity, last 12 months**

![Hungary: Daily market yields by maturity, last 12 months](results/market_yields/hungary/hungary_market_yields_12m.png)

**Bid-to-cover at every auction, last 12 months**

![Hungary: Bid-to-cover at every auction, last 12 months](results/auctions/hungary/hungary_recent_bid_to_cover_12m.png)

**Auction yields, 20 years (3-month average)**

![Hungary: Auction yields, 20 years (3-month average)](results/auctions/hungary/hungary_auction_yield_20y.png)

**Bid-to-cover, 20 years (3-month average)**

![Hungary: Bid-to-cover, 20 years (3-month average)](results/auctions/hungary/hungary_bid_to_cover_20y.png)

More: [every auction, last 12 months (with the market yield that day)](results/auctions/hungary/hungary_recent_auctions_12m.csv) · [daily market yields, last 12 months](results/market_yields/hungary/hungary_market_yields_12m.csv) · [monthly data, 20 years](results/auctions/hungary/hungary_auction_20y_monthly.csv) · [volume chart](results/auctions/hungary/hungary_accepted_20y.png)

</details>

<details>
<summary><b>Ireland</b> (auctions only)</summary>

**Every auction vs the daily market yield, last 12 months**

![Ireland: Every auction vs the daily market yield, last 12 months](results/auctions/ireland/ireland_recent_yield_12m.png)

**Bid-to-cover at every auction, last 12 months**

![Ireland: Bid-to-cover at every auction, last 12 months](results/auctions/ireland/ireland_recent_bid_to_cover_12m.png)

**Auction yields, 20 years (3-month average)**

![Ireland: Auction yields, 20 years (3-month average)](results/auctions/ireland/ireland_auction_yield_20y.png)

**Bid-to-cover, 20 years (3-month average)**

![Ireland: Bid-to-cover, 20 years (3-month average)](results/auctions/ireland/ireland_bid_to_cover_20y.png)

More: [every auction, last 12 months (with the market yield that day)](results/auctions/ireland/ireland_recent_auctions_12m.csv) · [monthly data, 20 years](results/auctions/ireland/ireland_auction_20y_monthly.csv) · [volume chart](results/auctions/ireland/ireland_accepted_20y.png)

</details>

<details>
<summary><b>Italy</b> (auctions only)</summary>

**Every auction vs the daily market yield, last 12 months**

![Italy: Every auction vs the daily market yield, last 12 months](results/auctions/italy/italy_recent_yield_12m.png)

**Bid-to-cover at every auction, last 12 months**

![Italy: Bid-to-cover at every auction, last 12 months](results/auctions/italy/italy_recent_bid_to_cover_12m.png)

**Auction yields, 20 years (3-month average)**

![Italy: Auction yields, 20 years (3-month average)](results/auctions/italy/italy_auction_yield_20y.png)

**Bid-to-cover, 20 years (3-month average)**

![Italy: Bid-to-cover, 20 years (3-month average)](results/auctions/italy/italy_bid_to_cover_20y.png)

More: [every auction, last 12 months (with the market yield that day)](results/auctions/italy/italy_recent_auctions_12m.csv) · [monthly data, 20 years](results/auctions/italy/italy_auction_20y_monthly.csv) · [volume chart](results/auctions/italy/italy_accepted_20y.png)

</details>

<details>
<summary><b>Lithuania</b> (auctions only)</summary>

**Every auction vs the daily market yield, last 12 months**

![Lithuania: Every auction vs the daily market yield, last 12 months](results/auctions/lithuania/lithuania_recent_yield_12m.png)

**Bid-to-cover at every auction, last 12 months**

![Lithuania: Bid-to-cover at every auction, last 12 months](results/auctions/lithuania/lithuania_recent_bid_to_cover_12m.png)

**Auction yields, 20 years (3-month average)**

![Lithuania: Auction yields, 20 years (3-month average)](results/auctions/lithuania/lithuania_auction_yield_20y.png)

**Bid-to-cover, 20 years (3-month average)**

![Lithuania: Bid-to-cover, 20 years (3-month average)](results/auctions/lithuania/lithuania_bid_to_cover_20y.png)

More: [every auction, last 12 months (with the market yield that day)](results/auctions/lithuania/lithuania_recent_auctions_12m.csv) · [monthly data, 20 years](results/auctions/lithuania/lithuania_auction_20y_monthly.csv) · [volume chart](results/auctions/lithuania/lithuania_accepted_20y.png)

</details>

<details>
<summary><b>Netherlands</b> (auctions only)</summary>

**Every auction vs the daily market yield, last 12 months**

![Netherlands: Every auction vs the daily market yield, last 12 months](results/auctions/netherlands/netherlands_recent_yield_12m.png)

**Auction yields, 20 years (3-month average)**

![Netherlands: Auction yields, 20 years (3-month average)](results/auctions/netherlands/netherlands_auction_yield_20y.png)

More: [every auction, last 12 months (with the market yield that day)](results/auctions/netherlands/netherlands_recent_auctions_12m.csv) · [monthly data, 20 years](results/auctions/netherlands/netherlands_auction_20y_monthly.csv) · [volume chart](results/auctions/netherlands/netherlands_accepted_20y.png)

</details>

<details>
<summary><b>Norway</b> (daily market yields)</summary>

**Every auction vs the daily market yield, last 12 months**

![Norway: Every auction vs the daily market yield, last 12 months](results/auctions/norway/norway_recent_yield_12m.png)

**Daily market yields by maturity, last 12 months**

![Norway: Daily market yields by maturity, last 12 months](results/market_yields/norway/norway_market_yields_12m.png)

**Bid-to-cover at every auction, last 12 months**

![Norway: Bid-to-cover at every auction, last 12 months](results/auctions/norway/norway_recent_bid_to_cover_12m.png)

**Auction yields, 20 years (3-month average)**

![Norway: Auction yields, 20 years (3-month average)](results/auctions/norway/norway_auction_yield_20y.png)

**Bid-to-cover, 20 years (3-month average)**

![Norway: Bid-to-cover, 20 years (3-month average)](results/auctions/norway/norway_bid_to_cover_20y.png)

More: [every auction, last 12 months (with the market yield that day)](results/auctions/norway/norway_recent_auctions_12m.csv) · [daily market yields, last 12 months](results/market_yields/norway/norway_market_yields_12m.csv) · [monthly data, 20 years](results/auctions/norway/norway_auction_20y_monthly.csv) · [volume chart](results/auctions/norway/norway_accepted_20y.png)

</details>

<details>
<summary><b>Poland</b> (auctions only)</summary>

**Every auction vs the daily market yield, last 12 months**

![Poland: Every auction vs the daily market yield, last 12 months](results/auctions/poland/poland_recent_yield_12m.png)

**Bid-to-cover at every auction, last 12 months**

![Poland: Bid-to-cover at every auction, last 12 months](results/auctions/poland/poland_recent_bid_to_cover_12m.png)

**Auction yields, 20 years (3-month average)**

![Poland: Auction yields, 20 years (3-month average)](results/auctions/poland/poland_auction_yield_20y.png)

**Bid-to-cover, 20 years (3-month average)**

![Poland: Bid-to-cover, 20 years (3-month average)](results/auctions/poland/poland_bid_to_cover_20y.png)

More: [every auction, last 12 months (with the market yield that day)](results/auctions/poland/poland_recent_auctions_12m.csv) · [monthly data, 20 years](results/auctions/poland/poland_auction_20y_monthly.csv) · [volume chart](results/auctions/poland/poland_accepted_20y.png)

</details>

<details>
<summary><b>Slovakia</b> (auctions only)</summary>

**Every auction vs the daily market yield, last 12 months**

![Slovakia: Every auction vs the daily market yield, last 12 months](results/auctions/slovakia/slovakia_recent_yield_12m.png)

**Bid-to-cover at every auction, last 12 months**

![Slovakia: Bid-to-cover at every auction, last 12 months](results/auctions/slovakia/slovakia_recent_bid_to_cover_12m.png)

**Auction yields, 20 years (3-month average)**

![Slovakia: Auction yields, 20 years (3-month average)](results/auctions/slovakia/slovakia_auction_yield_20y.png)

**Bid-to-cover, 20 years (3-month average)**

![Slovakia: Bid-to-cover, 20 years (3-month average)](results/auctions/slovakia/slovakia_bid_to_cover_20y.png)

More: [every auction, last 12 months (with the market yield that day)](results/auctions/slovakia/slovakia_recent_auctions_12m.csv) · [monthly data, 20 years](results/auctions/slovakia/slovakia_auction_20y_monthly.csv) · [volume chart](results/auctions/slovakia/slovakia_accepted_20y.png)

</details>

<details>
<summary><b>Slovenia</b> (auctions only)</summary>

**Every auction vs the daily market yield, last 12 months**

![Slovenia: Every auction vs the daily market yield, last 12 months](results/auctions/slovenia/slovenia_recent_yield_12m.png)

**Auction yields, 20 years (3-month average)**

![Slovenia: Auction yields, 20 years (3-month average)](results/auctions/slovenia/slovenia_auction_yield_20y.png)

More: [every auction, last 12 months (with the market yield that day)](results/auctions/slovenia/slovenia_recent_auctions_12m.csv) · [monthly data, 20 years](results/auctions/slovenia/slovenia_auction_20y_monthly.csv) · [volume chart](results/auctions/slovenia/slovenia_accepted_20y.png)

</details>

<details>
<summary><b>South Korea</b> (auctions only)</summary>

**Every auction vs the daily market yield, last 12 months**

![South Korea: Every auction vs the daily market yield, last 12 months](results/auctions/korea/korea_recent_yield_12m.png)

**Bid-to-cover at every auction, last 12 months**

![South Korea: Bid-to-cover at every auction, last 12 months](results/auctions/korea/korea_recent_bid_to_cover_12m.png)

**Auction yields, 20 years (3-month average)**

![South Korea: Auction yields, 20 years (3-month average)](results/auctions/korea/korea_auction_yield_20y.png)

**Bid-to-cover, 20 years (3-month average)**

![South Korea: Bid-to-cover, 20 years (3-month average)](results/auctions/korea/korea_bid_to_cover_20y.png)

More: [every auction, last 12 months (with the market yield that day)](results/auctions/korea/korea_recent_auctions_12m.csv) · [monthly data, 20 years](results/auctions/korea/korea_auction_20y_monthly.csv) · [volume chart](results/auctions/korea/korea_accepted_20y.png)

</details>

<details>
<summary><b>Spain</b> (daily market yields)</summary>

**Every auction vs the daily market yield, last 12 months**

![Spain: Every auction vs the daily market yield, last 12 months](results/auctions/spain/spain_recent_yield_12m.png)

**Daily market yields by maturity, last 12 months**

![Spain: Daily market yields by maturity, last 12 months](results/market_yields/spain/spain_market_yields_12m.png)

**Bid-to-cover at every auction, last 12 months**

![Spain: Bid-to-cover at every auction, last 12 months](results/auctions/spain/spain_recent_bid_to_cover_12m.png)

**Auction yields, 20 years (3-month average)**

![Spain: Auction yields, 20 years (3-month average)](results/auctions/spain/spain_auction_yield_20y.png)

**Bid-to-cover, 20 years (3-month average)**

![Spain: Bid-to-cover, 20 years (3-month average)](results/auctions/spain/spain_bid_to_cover_20y.png)

More: [every auction, last 12 months (with the market yield that day)](results/auctions/spain/spain_recent_auctions_12m.csv) · [daily market yields, last 12 months](results/market_yields/spain/spain_market_yields_12m.csv) · [monthly data, 20 years](results/auctions/spain/spain_auction_20y_monthly.csv) · [volume chart](results/auctions/spain/spain_accepted_20y.png)

</details>

<details>
<summary><b>Switzerland</b> (daily market yields)</summary>

**Every auction vs the daily market yield, last 12 months**

![Switzerland: Every auction vs the daily market yield, last 12 months](results/auctions/switzerland/switzerland_recent_yield_12m.png)

**Daily market yields by maturity, last 12 months**

![Switzerland: Daily market yields by maturity, last 12 months](results/market_yields/switzerland/switzerland_market_yields_12m.png)

**Bid-to-cover at every auction, last 12 months**

![Switzerland: Bid-to-cover at every auction, last 12 months](results/auctions/switzerland/switzerland_recent_bid_to_cover_12m.png)

**Auction yields, 20 years (3-month average)**

![Switzerland: Auction yields, 20 years (3-month average)](results/auctions/switzerland/switzerland_auction_yield_20y.png)

**Bid-to-cover, 20 years (3-month average)**

![Switzerland: Bid-to-cover, 20 years (3-month average)](results/auctions/switzerland/switzerland_bid_to_cover_20y.png)

More: [every auction, last 12 months (with the market yield that day)](results/auctions/switzerland/switzerland_recent_auctions_12m.csv) · [daily market yields, last 12 months](results/market_yields/switzerland/switzerland_market_yields_12m.csv) · [monthly data, 20 years](results/auctions/switzerland/switzerland_auction_20y_monthly.csv) · [volume chart](results/auctions/switzerland/switzerland_accepted_20y.png)

</details>

<details>
<summary><b>European Union</b> (auctions only)</summary>

**Every auction vs the daily market yield, last 12 months**

![European Union: Every auction vs the daily market yield, last 12 months](results/auctions/eu/eu_recent_yield_12m.png)

**Bid-to-cover at every auction, last 12 months**

![European Union: Bid-to-cover at every auction, last 12 months](results/auctions/eu/eu_recent_bid_to_cover_12m.png)

**Auction yields, 20 years (3-month average)**

![European Union: Auction yields, 20 years (3-month average)](results/auctions/eu/eu_auction_yield_20y.png)

**Bid-to-cover, 20 years (3-month average)**

![European Union: Bid-to-cover, 20 years (3-month average)](results/auctions/eu/eu_bid_to_cover_20y.png)

More: [every auction, last 12 months (with the market yield that day)](results/auctions/eu/eu_recent_auctions_12m.csv) · [monthly data, 20 years](results/auctions/eu/eu_auction_20y_monthly.csv) · [volume chart](results/auctions/eu/eu_accepted_20y.png)

</details>

### All countries, 20 years

![Government auction yields by country, 2006-2026](docs/images/global_auction_yield_grid_20y.png)

## Analysis: when and why yields shifted

The code in [`model_testing/`](model_testing/) analyses the results: it finds
the months where a country's auction yields moved to a new level, and checks
them against known events. It only reads the CSVs in `results/`, so rerun it
after each refresh of the data.

### Break detection (ruptures)

[`model_testing/breaks.py`](model_testing/breaks.py) uses
[ruptures](https://centre-borelli.github.io/ruptures-docs/) to find **break
dates**: months where a country's auction yields (or bid-to-cover) shifted to
a new level. Each break is matched against a list of known events, each
tagged with the countries it should affect. There are two lists:

- [`events_v2.csv`](model_testing/events_v2.csv) (main): **133 events**,
  2007-2026, including each country's own central bank turning points
  (first hike or cut of a cycle, QE, negative rates, currency floors),
  bailouts and budget crises, political shocks, wars and financial shocks.
  Every row has a source. It was built by two separate agents, one
  researching and one reviewing, neither of which saw any results, under
  rules fixed beforehand
  ([`event_rules.md`](model_testing/event_rules.md); how the two were
  merged: [`events_v2_decisions.md`](model_testing/events_v2_decisions.md)).
- [`events.csv`](model_testing/events.csv): the first list, 14 global and
  regional events (2008 crisis, euro crisis, COVID, Ukraine, 2022 hikes,
  Brexit and others), kept for comparison.

```bash
pip install -r model_testing/requirements.txt
python model_testing/breaks.py                         # auction yields, 2-10Y bucket, events.csv
python model_testing/breaks.py --events events_v2.csv  # the same against events_v2.csv
python model_testing/breaks.py --measure bid_to_cover
python model_testing/breaks.py --bucket Long --penalty 1
python model_testing/compare_llm.py                    # LLM breaks vs ruptures (below)
```

`--penalty` sets the sensitivity: higher means fewer, bigger breaks. Each
setting gets its own folder in [`model_testing/results/`](model_testing/results/)
(events.csv) or [`model_testing/results/events_v2/`](model_testing/results/events_v2/)
with a summary page, every break and every event check with its outcome,
recall by event, scores by country and a chart per country; each folder's
`README.md` compares all settings tested.

Months without an auction are filled in only across gaps of up to 6 months
(a straight line between the months either side). A longer gap splits a
country's series, and each stretch of at least 18 months is analysed on its
own, so nothing is invented across long gaps and no years are skipped.
Every month is tried as a break date.

#### How breaks are scored

Each break is matched to at most one event, and each event to at most one
break, within a window ([`scoring.py`](model_testing/scoring.py)): **±3
months for events_v2.csv**, ±6 for events.csv. events_v2.csv has about one
event per country per year, so with ±6 months random dates would match an
event about 72% of the time and the test couldn't tell a good model from
guessing; at ±3 it's about 45%. An event is checked when it falls inside a
stretch of the country's data.

| Term | Meaning here |
|---|---|
| True positive (TP) | a break matched to a known event |
| False positive (FP) | a break with no event left to match (a lead, or noise) |
| False negative (FN) | a known event with no break matched to it (missed) |
| Precision | TP / (TP + FP): share of breaks that match an event |
| Recall | TP / (TP + FN): share of events detected |
| F1 | 2 × precision × recall / (precision + recall) |
| Random baseline | the same number of breaks per stretch at random dates, scored the same way (1,000 draws) |
| p-value | share of random draws with an F1 at least as high as the real one |

Accuracy isn't used: it needs true negatives (months with neither a break
nor an event), and almost every month is one. A model that never finds a
break would score 92% accuracy here (97% on the old list).

#### Results

Data of 22 November 2026; auction yields, 2–10 year bucket, penalty 2;
59 breaks in 22 countries, scored against events_v2.csv (355 country-event
pairs checked):

| | Ruptures | Random baseline |
|---|:-:|:-:|
| Precision | **66%** (39 TP of 59 breaks) | 45% |
| Recall | **11%** (39 TP of 355 events) | 8% |
| F1 | **0.19** | 0.13 |

39 TP, 20 FP, 316 FN; p-value ≤ 0.001 (no random draw did as well).

![Precision vs recall for each setting, events_v2.csv](model_testing/results/events_v2/settings_comparison.png)

| Setting | events_v2.csv (±3 months): TP / FP / FN | Precision | Recall | F1 | Random F1 | events.csv (±6): TP / FP / FN | F1 | Random F1 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Yields 2–10Y, penalty 0.5 | 84 / 38 / 271 | 69% | 24% | 0.35 | 0.23 | 65 / 57 / 71 | 0.50 | 0.27 |
| Yields 2–10Y, penalty 1 | 63 / 29 / 292 | 68% | 18% | 0.28 | 0.19 | 50 / 42 / 86 | 0.44 | 0.24 |
| Yields 2–10Y, penalty 2 | 39 / 20 / 316 | 66% | 11% | 0.19 | 0.13 | 37 / 22 / 99 | 0.38 | 0.19 |
| Yields 10Y+, penalty 2 | 47 / 21 / 274 | 69% | 15% | 0.24 | 0.15 | 34 / 34 / 84 | 0.37 | 0.20 |
| Bid-to-cover 2–10Y, penalty 2 | 3 / 8 / 309 | 27% | 1% | 0.02 | 0.03 | 3 / 8 / 113 | 0.05 | 0.05 |

- **Ruptures finds real turning points, but only the big ones.** About two
  thirds of its breaks are within 3 months of an event (random: 45%), and
  every yield setting beats random (p ≤ 0.001). But recall is low: most
  events in the longer list (a country's first 25bp cut, a rating change)
  don't move 2–10 year yields enough, next to each country's 20-year
  range, to show up as a break.
- **Penalty 0.5 has the best F1** on both lists; penalty 2 finds fewer
  breaks at about the same precision.
- **Recall by type of event** (penalty 2): geopolitical 17%, political
  13%, monetary 12%, financial 8%, fiscal 6%. At penalty 0.5 geopolitical
  rises to 38%.
- **Big misses:** COVID (0 of 19 countries), SVB and Credit Suisse 2023
  (0 of 19), the 2007 credit crunch (0 of 13), the 2010 Greek bailout
  (0 of 9) and Trump's 2016 election (1 of 19). Best: Lehman (5 of 13) and
  Ukraine with the 2022 hikes (6 of 19).
- **The merge rule costs some matches:** events less than 3 months apart
  are one event, dated at the first. The Fed's first hike (Mar 2022) is
  merged into the Ukraine invasion (Feb 2022), so the US break of June
  2022 is more than 3 months from it and counts as an FP.
- **Bid-to-cover is no better than random** on either list (p = 0.94 and
  0.67), so demand breaks have other causes.
- **False positives** are the leads: Norway March 2010, Japan December
  2014, Hungary June 2014, Finland 2017 and 2018, Switzerland August 2024
  and others in `breaks.csv`.
- **On the old 14-event list** the same breaks score F1 0.38 (random
  0.19), with recall capped by events weeks apart (the Ukraine invasion
  and the Fed's first hike count as two events there).

### LLM analysis vs ruptures

As an independent check, an LLM (Claude Opus 5.5) read the same monthly
yields and marked its own break dates and causes before ruptures was rerun.
Details: [`model_testing/results/llm_analysis/`](model_testing/results/llm_analysis/).

![Ruptures and the LLM scored against events and against each other](model_testing/results/llm_analysis/llm_vs_ruptures.png)

| Against events_v2.csv (±3 months) | TP | FP | FN | Precision | Recall | F1 | Random F1 | p-value |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Ruptures (penalty 2) | 39 | 20 | 316 | 66% | 11% | 0.19 | 0.13 | 0.003 |
| LLM, all breaks ruptures could see (133) | 93 | 40 | 262 | 70% | 26% | 0.38 | 0.25 | ≤ 0.001 |
| LLM, high confidence (56) | 54 | 2 | 301 | 96% | 15% | 0.26 | 0.13 | ≤ 0.001 |
| LLM, medium confidence (58) | 29 | 29 | 326 | 50% | 8% | 0.14 | 0.13 | 0.26 |
| LLM, low confidence (19) | 10 | 9 | 345 | 53% | 3% | 0.05 | 0.05 | 0.32 |

- **The LLM's high-confidence breaks are almost all real events:** 54 of
  56 are within 3 months of one (random: 46%). On the old list it was 71%,
  because most of its causes are a country's own central bank or politics,
  which that list didn't have. Its medium and low-confidence breaks are no
  better than random. Caveat: the LLM picked its breaks knowing the same
  history the events come from, so this isn't a fully independent test.
- **Agreement, the LLM's list as reference** (±6 months): ruptures at
  penalty 2 has 49 TP, 10 FP and 84 FN: precision 83% (its breaks are
  mostly in the LLM's list), recall 37% (it finds about a third of the
  LLM's breaks), F1 0.51. At penalty 0.5 the F1 is 0.71. For the 35 pairs
  where ruptures' break matches an event, the LLM's cause is dated within 3
  months of that event in 20.
- **Fewer mislabelled events:** with country events in the list, the
  Czech break in November 2021 is no longer credited to the Ukraine
  invasion (it came before it); it is now an FP, just over 4 months after
  the CNB's first hike (June 2021).
- **Data error found:** Finland's 17 November 2026 auction is published at a
  3,389% yield; values like that are now left out as typos (see Caveats).

## Run it

```bash
pip install -r requirements.txt
python treasurydata.py
```

Each run creates a dated folder, with auction results and market yields kept
apart (they come from different sources):

```
runs/2026-11-22_083520_20y/
  auctions/
    auction_totals.csv          auctions per country and maturity bucket
    us/  canada/  france/ ...   one folder per country: charts + CSVs
    global/                     every country together
  market_yields/
    us/  canada/  uk/ ...       daily market yields: chart + CSV (10 countries)
    global/                     all of them together
```

Change the lookback windows with `YEARS` (20-year charts) and `RECENT_MONTHS`
(per-auction charts) at the top of `treasurydata.py`.
If one country's website is down, the run prints a warning and carries on.

## What the charts show

| Measure | Meaning |
|---|---|
| **Bid-to-cover** | Total bids ÷ amount sold. Higher = more competition for the debt. |
| **Volume** | Gross amount sold at auction, in local currency (not net new borrowing). |
| **Auction yield** | The interest rate the auction cleared at (or the average accepted yield, depending on the country). |
| **Central bank share** | Central bank purchases at auction ÷ amount sold. Most central banks are legally barred from buying at their own government's auctions, so this exists only where it actually happens. |
| **Market yield** | The yield on existing bonds as they trade between investors each day (what news sites quote as "the 10-year yield"). Auctions sell new bonds at close to this rate on the day. |

**Last 12 months (`_recent_..._12m` files): no averaging.** Each dot is one
auction; the line is the daily market yield for the same maturity. Auctions
are grouped into panels by maturity (1-month, 3-month, ..., 10-year, 30-year;
an auction goes in the nearest panel within 25%). The `_recent_auctions_12m.csv`
file lists every auction with the market yield that day and the gap in basis
points: an auction clearing **above** the market (a "tail") means buyers
needed a sweetener, **below** means strong demand.

**20 years (`_20y` files): monthly averages.** Auctions are grouped by time to
maturity: **Short** (≤2 years), **Intermediate** (2–10 years), **Long**
(>10 years). Monthly figures are medians (bid-to-cover, yield) or sums
(volume), smoothed with a 3-month rolling average over calendar months (this
month and the two before, using whichever had auctions). Where a series has
no auctions for more than 6 months the line stops, so gaps show as gaps; a
month with no neighbour is drawn as a dot. The 20-year charts and monthly
CSVs stop at the last full month: the current month's auctions appear only
on the 12-month charts. When a source stops partway through a month (no
auction for much longer than usual, e.g. the US data ending on 15 October
2026), that month is left out too and the run log says so.

Countries define these measures slightly differently (e.g. clearing vs average
yield), so compare **trends** across countries more than exact levels.

On the global charts each country has a fixed colour and line style (eight
colours × solid/dashed/dotted/dash-dot), so it looks the same on every chart and run.
The `_grid` versions give each country its own small panel instead.

## Example charts

These come from the run of 22 November 2026. Each run writes its own copies to
`runs/`; the images here are just a snapshot for this page.

**Demand at auction, all countries.** Bid-to-cover by maturity, one line per
country. The spike is Japan in 2012-13, when bill yields were stuck at the Bank
of Japan's 0.1% floor and bids reached over 20 times the amount sold.

![Bid-to-cover, all countries](docs/images/global_bid_to_cover_20y.png)

**Central bank share of auctions.** Only the Fed and the Bank of Canada buy at
their own government's auctions. The Bank of Canada's fixed shares (20%, then
15%, 13%) stop in 2022 when it ended bond purchases at auction; the Fed's share
follows its maturing holdings, which it reinvests at auction.

![Central bank share of auction awards](docs/images/global_central_bank_share_20y.png)

**One country in detail: United States.** Every country gets its own folder of
charts like this one, plus a monthly CSV.

![United States bid-to-cover by maturity](docs/images/us_bid_to_cover_20y.png)

**European Union.** The EU's own EU-Bills and EU-Bonds, auctioned by the
European Commission since 2021: yields rose from below zero to around 3-4% as
the ECB raised rates in 2022-23.

![European Union auction yields](docs/images/eu_auction_yield_20y.png)

## Coverage

### Included (24 countries + the EU)

| Country | Source | From | Bid-to-cover | Yield used | Central bank share | Notes |
|---|---|---|:-:|---|:-:|---|
| United States | U.S. Treasury Fiscal Data API | 2006 | ✓ | Clearing (high yield) | ✓ (Fed) | Also non-primary-dealer share |
| Canada | Bank of Canada Valet API | 2006 | ✓ | Clearing (high yield) | ✓ (BoC) | |
| United Kingdom | UK Debt Management Office | 2006 | ✓ | Average (yield at average accepted price) | | Gilts only; T-bills are sold separately |
| Germany | Finanzagentur | 2006 | ✓ | Average (weighted average yield) | | |
| Japan | Ministry of Finance | 2006 | ✓ | Clearing (yield at lowest accepted price) | | Published with a ~1 month lag. No 3-month bills before Feb 2009 (the MOF file only has them from when financing bills and T-bills were merged), so short-term counts and volume jump then |
| Austria | OeKB (auction agent) | 2007 | | Issue yield (as published) | | Bonds only; total bids not published |
| Belgium | Belgian Debt Agency | 2006 | ✓ | Average (weighted average yield) | | Parsed from PDFs |
| Czech Republic | Czech National Bank | 2006 | ✓ | Clearing (maximum accepted yield); bills: average | | T-bill data ends in 2021 (no later file published). The Ministry of Finance's purchases of its own bills (large in 2020–21) are left out of bid-to-cover and volume, as for bonds, and kept in an `issuer_retained` column; bill cover = investor bids ÷ the larger of the amount offered and the amount sold. The few euro-denominated bonds (2022, 2024) are excluded |
| Denmark | Danmarks Nationalbank | 2008 | ✓ | Clearing (cut-off price/rate) | | Current year read from the results pages |
| Finland | State Treasury open data API | 2006 | ✓ | Issue yield (as published) | | Mostly syndications before 2019 |
| France | Agence France Trésor | 2006 | ✓ | Average (weighted average rate) | | |
| Greece | Public Debt Management Agency | 2008 | ✓ | Uniform price (clearing = average) | | Bills only (bonds mostly syndicated) |
| Hungary | ÁKK (via its website's data API) | 2006 | ✓ | Clearing (maximum accepted yield) | | |
| Ireland | NTMA | 2009 | ✓ | Issue yield (as published) | | Bill history ends in 2022 |
| Italy | Banca d'Italia | 2006 | ✓ | Allotment yield (see note) | | |
| Lithuania | Nasdaq Baltic (Vilnius auctions) | 2008 | ✓ | Clearing (maximum accepted yield) | | Maturities looked up per bond on Nasdaq Baltic. Amounts before 2015 are all labelled EUR by the source, but litas bonds' amounts look like unconverted litas (round figures; the source doesn't say which bonds), so the volume chart before 2015 may be overstated up to ~3.45×; bid-to-cover and yields are unaffected |
| Netherlands | Dutch State Treasury Agency | 2007 | | Issue yield (as published) | | Bids not published |
| Norway | Norges Bank | 2006 | ✓ | Issue yield (as published) | | |
| Poland | Ministry of Finance | 2006 | ✓ | Clearing (maximum accepted yield) | | |
| Slovakia | ARDAL | 2009 | ✓ | Clearing (maximum accepted yield) | | Bonds only; parsed from per-auction PDFs (the 2009–2016 ones label the clearing yield "maximum interest rate"). Non-competitive top-ups and buy-backs excluded |
| Slovenia | Ministry of Finance | 2007 | | Issue rate (as published) | | Bills only; bids not published |
| South Korea | Ministry of Economy and Finance (KTB site) | 2018 | ✓ | Clearing (highest accepted rate) | | KTB bonds only; the English results pages start in 2018 |
| Spain | Tesoro Público | 2025 | ✓ | Clearing (stop-out/marginal rate) | | Only the last two years are published in bulk |
| Switzerland | Federal Finance Administration / SNB | 2010 | ✓ | Uniform price (clearing = average) | | Bonds, plus money market claims (bills) from 2012 |
| **European Union** (not a country) | European Commission | 2021 | ✓ | Average (weighted average yield) | | EU-Bonds and EU-Bills; see below |

**European Union.** The EU borrows in its own name (e.g. for NextGenerationEU),
with auctions run by the European Commission since September 2021. It's
treated like a country, with its own `eu/` folder and a place on the global
charts. The ECB is the euro area's central bank but, like the national central
banks, is barred from buying at primary auctions, so there's no central bank
share. The Commission publishes one web page per auction, so the first run
fetches a few hundred pages slowly (the site rate-limits) and caches them in
`cache/`; later runs only fetch new auctions.

**Yield used:**
- **Clearing:** the highest yield accepted, i.e. the auction's cut-off. Every
  winning bidder got that yield or a lower one.
- **Average:** the weighted average of all accepted bids, which sits slightly
  below the clearing yield.
- **Uniform price:** every winner pays the same price, so clearing and average are
  the same number.
- **Issue yield (as published):** the source gives one yield per auction without
  saying whether it is the clearing or the average yield.
- **Italy:** the allotment yield is the clearing yield for bonds, which are sold at
  a single price, and the weighted average yield for BOT bills.

Inflation-linked and floating-rate securities are excluded everywhere (as US
TIPS and FRNs are), because they don't quote comparable nominal yields.

### Daily market yields (10 countries)

Official, free daily sources, used for the lines on the 12-month charts:

| Country | Source | Maturities | Notes |
|---|---|---|---|
| United States | U.S. Treasury daily par yield curve | 1 month – 30 years | |
| Canada | Bank of Canada (Valet API) | 3 months – 30 years | T-bill and benchmark bond yields |
| United Kingdom | Bank of England nominal par yields | 5, 10, 20 years | Only three maturities are published daily |
| Germany | Bundesbank yield curve for Federal securities | 1 – 30 years | Fitted curve (Svensson method) |
| Japan | Ministry of Finance JGB interest rates | 1 – 40 years | |
| Belgium | National Bank of Belgium OLO reference rates | 1 – 30 years | |
| Hungary | ÁKK benchmark yields | 3 months – 20 years | Average of primary dealer quotes |
| Norway | Norges Bank generic government yields | 3 – 10 years | |
| Spain | Banco de España daily indicators | 1 – 30 years | |
| Switzerland | SNB spot rates on Confederation bonds | 1 – 30 years | Zero-coupon rates; **updated monthly**, so the latest few weeks are missing |

The other 14 show auctions only. The euro-area countries' daily yields aren't
published free by their central banks or the ECB (which publishes monthly
averages per country, and daily figures only for the euro area as a whole).
France's Banque de France and South Korea's Bank of Korea need a free API key;
the rest have no free daily download.

### Not included yet (14 countries)

| Country | Why |
|---|---|
| Australia | AOFM's site doesn't respond to automated downloads |
| New Zealand | Debt Management site sits behind a browser-only bot check (Cloudflare) |
| Sweden | Riksgälden's auction statistics are only in an interactive QlikView dashboard |
| Portugal | IGCP's site blocks automated requests (HTTP 403) |
| Mexico | Full history needs a free Banxico SIE API token |
| Turkey | Results are one PDF per auction; bulk data needs a free CBRT EVDS API key |
| Israel | Results are published on Bloomberg; no bulk public download found |
| Chile | Historical files on the Finance Ministry's old site stop in 2020 |
| Colombia | No bulk download of TES auction results found |
| Iceland | Results are one web page/PDF per auction |
| Latvia | Results are only in individual news releases |
| Estonia | Very little domestic auction issuance |
| Luxembourg | Issues by syndication, not auction |
| Costa Rica | No bulk download found |

Countries marked "needs a free API key" can be added once a key is available.

## Project layout

```
treasurydata.py      entry point: runs every country, writes the run folder
common.py            shared bucketing, monthly aggregation and charts
countries/
  __init__.py        list of countries to run
  _http.py           download helpers
  <country>.py       one loader per country (eu.py for the European Union)
cache/               downloaded auction pages and lookups for the EU, South Korea,
                     Slovakia and Lithuania (gitignored); rebuilt automatically
results/             copy of the latest run (auctions/ and market_yields/)
docs/images/         example charts shown in this README
model_testing/       analysis of results/: break detection (breaks.py), the
                     LLM comparison (compare_llm.py), scoring (scoring.py) and known
                     events (events_v2.csv, events.csv, with how they were made);
                     its own results/ and requirements.txt
```

### Adding a country

Write `countries/<name>.py` with a `fetch(start, end)` function that returns one
row per auction with these columns, plus a `COUNTRY` describing it (see any
existing loader), then add it to `countries/__init__.py`:

| Column | Meaning |
|---|---|
| `auction_date` | Date of the auction |
| `maturity_date` | Date the security is repaid |
| `bid_to_cover` | Total bid ÷ amount sold (NaN if not published) |
| `accepted` | Amount sold, in local currency units |
| `auction_yield` | Yield in percent (NaN if not published) |
| `cb_accepted` | Central bank purchases at the auction (NaN if none or not reported) |

Charts for any measure a country doesn't publish are skipped automatically.

## Caveats

- Several sources aren't formal APIs (Hungary's website data endpoint, Belgium's
  and Slovakia's PDFs, Greece's web tables, the EU's and South Korea's
  per-auction pages), so a site redesign can break a loader. When that
  happens the run reports the failure for that country and continues.
- The first run downloads a few thousand pages and PDFs for the EU, South Korea
  and Slovakia, pacing requests to respect the sites' limits, so it takes
  about half an hour. Later runs read `cache/` and only fetch new auctions.
- Volumes are in each country's own currency, so the global charts compare
  bid-to-cover, yields and central bank share, not volume.
- Market yields and auction yields aren't defined identically (par, benchmark
  or zero-coupon curves vs one specific bond's clearing or average yield), so a
  few basis points between line and dot is normal. The UK gap is a little
  larger because the DMO's file gives only each gilt's maturity year.
- Sources occasionally publish typos. Yields outside −3% to 25% and
  bid-to-cover above 50 are treated as typos and left out (the run log
  counts them), e.g. Finland's 17 November 2026 auction, published at a
  3,389% yield. Some loaders also cross-check: South Korea's amount bid is
  checked against the page's own ratio, and Slovak amounts with malformed
  digit groups ("339 700 0000") are rejected.
- A source that stops updating is flagged in the run log (latest auction
  more than 45 days old, or market yield more than 10 days old).
