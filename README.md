# Polkadex Open Beta

**Introduction**

With the singular goal in mind to make our products better by taking into account the widest possible community feedback, we are introducing a new program called the ‘Polkadex Open Beta.’ This program will give the wider Polkadex community a chance to test Polkadex products and updates pre-launch, provide feedback and earn rewards for helping the Polkadex team deliver better versions of the products originally envisioned. While we are shifting to this new model of beta testing to keep the feedback and the rewards as fair and transparent as possible, this is still a pilot program designed to evolve and improve as we go. We’re building together. In this sense, your feedback is not only crucial to creating a better product, but it’s also essential to making the most of the open beta program. If you have any suggestions for improving the beta experience, let us know.

****Guidelines****

1. Anyone is welcome to try out the products deployed onto the public Polkadex testnet
2. If you find any bugs that the team might have missed or if you feel that something can be improved, you are encouraged to log an issue with your feedback on this GitHub repository
3. Provide your Polkadex Blockchain account Address that has a verified On-chain identity in the following format onchainaddress:{Insert your onchain address within the braces} at the end of the description of each issue you log
4. The Polkadex team will constantly evaluate logged issues and rate them as 'Critical,' 'Moderate' or 'Normal' based on their severity or their value-add to the product
5. The team will evaluate the feedback in cycles of 45 day periods to provide these ratings
6. Polkadex Inc will put a Polkadex Treasury Proposal for $3,500 worth of PDEX to form a rewards pool before the beginning of every feedback cycle
7. If the treasury proposal is approved, the upcoming feedback cycle will be a Rewarded Cycle
8. If the treasury proposal is denied, the upcoming feedback cycle will be an Unrewarded Cycle
9. The Polkadex team will announce if a cycle is Rewarded or Unrewarded through Polkadex’s social media channels
10. Once every 45 days, all the participants who have logged feedback and received ratings will split rewards evenly from the Open Beta PDEX reward pool if the feedback cycle is a 'Rewarded Cycle,' based on the levels as described in the below table
11. After a 45 day cycle ends, the team will finish rating the issues logged during that cycle within the next 45 days and announce the tallies
12. Beta Tester agrees that the rating given by Polkadex will be final and undisputable
13. Your total rewards earned will be updated on GitHub/released through our social media channel at a later time with your on-chain identity
14. Only issues with Blockchain Addresses that have a verified On-chain identity will be accepted by Polkadex and will be considered for rewards
15. Once the ratings are finalized and rewards are calculated, the Polkadex team will let you know the procedure for obtaining the rewards
16. The cycle restarts again on the 46th day
17. By participating in the program, you agree to the terms & conditions listed herein
18. Note: Currently, testers based in the USA are restricted from receiving beta tester rewards based on SEC regulations. Please read T&C carefully.

**Reward Model**

| Level | Reward Pool (worth of PDEX) | Distribution Timeline |
| --- | --- | --- |
| 1. Critical (⭐️ ⭐️ ⭐️)  | $2000 | 45 Days |
| 2. Moderate (⭐️ ⭐️) | $1000 | 45 Days |
| 3. Normal (⭐️) | $500 | 45 Days |
| 4. Acknowledgement | N/A | N/A |

**Description of Levels**

**Level 1**

1. High-level vulnerabilities that are difficult to exploit; however, that have a significant impact on the system. Critical user experience issues.
    1. Ex: Balance not updating
    2. Ex: Not receiving notifications

**Level 2**

1. Medium-level vulnerabilities that are important to fix; however, that cannot lead to assets loss or data manipulations.
    1. Ex: Orderbook not accepting orders
    2. Ex: New investors not being able to participate in the rounds

**Level 3**

1. Suggestions we can consider to implement in the future. Not critical but nice to have fixes
    1. Ex: UI improvements

**Level 4**

1. Issues we are already aware of and have chosen to fix in subsequent iterations

**Important**

1. Please note that the rating is subjective. It is based on the team’s view of how valuable the feedback is to the product. The team’s rating will be final. Sometimes during development, we may leave some parts pending intentionally to add in future iterations based on our timelines and availability of resources. If you happen to log those as a bug, we may only ‘acknowledge’ them as we are already aware of them.
2. If you find a bug that is very critical and can cause potential loss of assets from the system, please don’t log it on the public repo. Please reach out to the team personally or log it on the ‘Bug Bounty Program’ which will be live soon on a major bug bounty platform [Immunefi](https://immunefi.com/).

**Top Testers**

1. On top of the above rewards, the top three testers in each period will receive a bonus percentage of rewards on top of the eligible rewards as described below:
    
    
    | Rank | Bonus |
    | --- | --- |
    | 1 | 20% |
    | 2 | 10% |
    | 3 | 5% |

**Note**

Top Tester rewards will be introduced when the team deems that there's a significant number of people participating in the program. The team will activate or discontinue the Top Tester rewards as and when required based on participation. The team's decision is final and will be communicated through our social media channels when the Top Tester rewards are active.

**Contact**

1. You can contact us through our discord/telegram channel for any questions/concerns related to the program [here](https://discord.gg/mVvTSBE3JY)

Known Critical Issues: 
1. Accounts are removed by clearing browser cache/using 'remove from browser option.' But they are not removed from the blockchain. Once the 3 accounts limit is reached, this will throw a proxy limit reached error. New proxy created after clearing the old proxies from blockchain instead of frontend doesn’t work. New Accounts created won’t show up.
2. UI: Remove Proxy Account window doesn't have a close option. Real time updates at various places need to be added. Recent Trades component needs to be refactored.
