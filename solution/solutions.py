# -*- coding: utf-8 -*-


def solution_1124(*args, **kwargs):
    def longestWPI(hours):
        res = score = 0
        seen = {}
        for i, h in enumerate(hours):
            score = score + 1 if h > 8 else score - 1
            if score > 0:
                res = i + 1
            seen.setdefault(score, i)
            if score - 1 in seen:
                res = max(res, i - seen[score - 1])
        return res

    return longestWPI(*args)


def solution_1125(*args, **kwargs):
    # https://leetcode.com/problems/smallest-sufficient-team/
    def smallestSufficientTeam_1125(req_skills, people):
        n = len(req_skills)
        # 用位置表示技能
        key = {v: i for i, v in enumerate(req_skills)}
        # 零值用来启动循环
        dp = {0: []}
        for i, p in enumerate(people):
            his_skill = 0
            for skill in p:
                if skill in key:
                    # 某人在结果中有某个技能，用位图表示，左移一是代入0索引的值
                    his_skill |= 1 << key[skill]

            # python3, 更新字典问题
            update_dp = {}
            for skill_set, need in dp.items():
                # 遍历字典，如果某人在结果中的技能与已记录的技能组合（键）做并
                with_him = skill_set | his_skill
                # 如果没有变化，则路过继续
                if with_him == skill_set:
                    continue
                # 如果没有记录或者新的组合所需的人更少，则更新值（人的组合）
                if with_him not in dp and with_him not in update_dp:
                    update_dp[with_him] = need + [i]
                    continue

                if with_him in dp and len(dp[with_him]) > len(need) + 1:
                    update_dp[with_him] = need + [i]
                    continue

                if with_him in update_dp and len(update_dp[with_him]) > len(need) + 1:
                    update_dp[with_him] = need + [i]
                    # dp[with_him] = need + [i]
            dp.update(update_dp)
        return dp[(1 << n) - 1]

    return smallestSufficientTeam_1125(*args)


if __name__ == '__main__':
    result = solution_1124([9, 1, 1, 9, 9, 9, 9, 9, 1, ])
    print(result)
