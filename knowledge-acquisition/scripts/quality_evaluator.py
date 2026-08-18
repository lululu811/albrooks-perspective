#!/usr/bin/env python3
"""
质量评估器 - 评估信息源质量

负责：
1. 计算可信度评分
2. 识别来源类型
3. 检测偏见
4. 执行交叉验证
"""

import yaml
import re
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass

@dataclass
class QualityAssessment:
    """质量评估结果"""
    credibility_score: float
    source_type: str  # primary/secondary/speculative
    bias_detected: List[str]
    cross_validation_passed: bool
    recommendations: List[str]

class QualityEvaluator:
    """质量评估器"""

    def __init__(self, config_dir: Path):
        self.config_dir = config_dir
        self.rules = self._load_config("quality-rules.yaml")

    def _load_config(self, filename: str) -> Dict:
        """加载配置文件"""
        config_path = self.config_dir / filename
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def assess_source(self, source: Dict) -> QualityAssessment:
        """评估单个信息源"""
        # 1. 计算可信度评分
        credibility_score = self._calculate_credibility(source)

        # 2. 识别来源类型
        source_type = self._identify_source_type(source)

        # 3. 检测偏见
        bias_detected = self._detect_bias(source)

        # 4. 生成建议
        recommendations = self._generate_recommendations(
            credibility_score, source_type, bias_detected
        )

        return QualityAssessment(
            credibility_score=credibility_score,
            source_type=source_type,
            bias_detected=bias_detected,
            cross_validation_passed=False,  # 需要多个来源才能验证
            recommendations=recommendations
        )

    def _calculate_credibility(self, source: Dict) -> float:
        """计算可信度评分"""
        scoring_config = self.rules['credibility_scoring']

        # 基础分
        base_score = 0
        source_url = source.get('url', '')

        # 判断来源类型
        if self._is_primary_source(source):
            base_score = scoring_config['base_scores']['primary_source']
        elif self._is_authoritative_media(source_url):
            base_score = scoring_config['base_scores']['authoritative_media']
        elif self._is_social_media(source_url):
            base_score = scoring_config['base_scores']['social_media']
        else:
            base_score = scoring_config['base_scores']['secondary_source']

        # 检查黑名单
        if self._is_blacklisted(source_url):
            return 0

        # 调整分
        adjustments = scoring_config['adjustments']
        score = base_score

        if source.get('has_recording'):
            score += adjustments['has_recording']
        if source.get('has_citation'):
            score += adjustments['has_citation']
        if not source.get('has_source'):
            score += adjustments['no_source']
        if source.get('is_self_promotion'):
            score += adjustments['self_promotion']
        if source.get('has_conflict_of_interest'):
            score += adjustments['conflict_of_interest']

        return max(0, min(100, score))

    def _identify_source_type(self, source: Dict) -> str:
        """识别来源类型"""
        content = source.get('content', '')
        source_type_rules = self.rules['source_types']

        for source_type, config in source_type_rules.items():
            patterns = config.get('patterns', [])
            for pattern in patterns:
                if re.search(pattern, content):
                    return source_type

        return 'secondary'  # 默认

    def _detect_bias(self, source: Dict) -> List[str]:
        """检测偏见"""
        bias_detected = []
        content = source.get('content', '')
        bias_config = self.rules['bias_detection']

        # 媒体偏见
        for indicator in bias_config['media_bias']['indicators']:
            if indicator in content:
                bias_detected.append(f"媒体偏见: {indicator}")
                break

        # 自我报告偏见
        for indicator in bias_config['self_reporting_bias']['indicators']:
            if indicator in content:
                bias_detected.append(f"自我报告偏见: {indicator}")
                break

        # 幸存者偏差
        for indicator in bias_config['survivorship_bias']['indicators']:
            if indicator in content:
                bias_detected.append(f"幸存者偏差: {indicator}")
                break

        return bias_detected

    def _generate_recommendations(
        self,
        credibility_score: float,
        source_type: str,
        bias_detected: List[str]
    ) -> List[str]:
        """生成建议"""
        recommendations = []

        if credibility_score < 40:
            recommendations.append("❌ 可信度低，建议寻找更可靠的来源")
        elif credibility_score < 60:
            recommendations.append("⚠️  可信度中等，建议交叉验证")
        else:
            recommendations.append("✅ 可信度高，可以使用")

        if source_type == 'speculative':
            recommendations.append("🔍 推测性来源，需要更多证据")

        if bias_detected:
            recommendations.append(f"⚖️  检测到偏见: {', '.join(bias_detected)}")

        return recommendations

    def cross_validate(self, sources: List[Dict]) -> Tuple[bool, List[str]]:
        """交叉验证多个来源"""
        validation_rules = self.rules['cross_validation']

        # 检查来源数量
        if len(sources) < validation_rules['min_sources']:
            return False, [f"来源数量不足（需要≥{validation_rules['min_sources']}个）"]

        # 检查来源类型多样性
        source_types = set(self._identify_source_type(s) for s in sources)
        if len(source_types) < validation_rules['min_source_types']:
            return False, [f"来源类型单一（需要≥{validation_rules['min_source_types']}种）"]

        # 检查时间跨度
        # 这里需要实现时间跨度检查逻辑
        time_span_ok = True
        if not time_span_ok:
            return False, ["时间跨度不足"]

        return True, ["✅ 交叉验证通过"]

    def _is_primary_source(self, source: Dict) -> bool:
        """判断是否为一手来源"""
        return source.get('is_primary', False)

    def _is_authoritative_media(self, url: str) -> bool:
        """判断是否为权威媒体"""
        authoritative_domains = [
            'caixin.com', 'latepost.com', '36kr.com',
            'huxiu.com', 'bloomberg.com', 'reuters.com'
        ]
        return any(domain in url for domain in authoritative_domains)

    def _is_social_media(self, url: str) -> bool:
        """判断是否为社交媒体"""
        social_domains = ['twitter.com', 'weibo.com', 'xueqiu.com']
        return any(domain in url for domain in social_domains)

    def _is_blacklisted(self, url: str) -> bool:
        """检查是否在黑名单中"""
        blacklist = ['zhihu.com', 'mp.weixin.qq.com', 'baike.baidu.com']
        return any(domain in url for domain in blacklist)


# 使用示例
if __name__ == "__main__":
    config_dir = Path(__file__).parent.parent / "config"
    evaluator = QualityEvaluator(config_dir)

    # 示例信息源
    source = {
        'url': 'https://caixin.com/article/123',
        'content': '原文：芒格说...',
        'has_recording': True,
        'has_citation': True,
        'is_primary': True
    }

    assessment = evaluator.assess_source(source)
    print(f"可信度评分: {assessment.credibility_score}")
    print(f"来源类型: {assessment.source_type}")
    print(f"偏见检测: {assessment.bias_detected}")
    print(f"建议: {assessment.recommendations}")
