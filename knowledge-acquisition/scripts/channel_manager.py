#!/usr/bin/env python3
"""
渠道管理器 - 管理知识获取渠道

负责：
1. 加载渠道配置
2. 根据人物类型选择渠道
3. 执行渠道搜索
4. 处理渠道失败和降级
"""

import yaml
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class SearchResult:
    """搜索结果"""
    channel: str
    url: str
    title: str
    content: str
    credibility_score: float
    source_type: str  # primary/secondary/speculative
    metadata: Dict

class ChannelManager:
    """渠道管理器"""

    def __init__(self, config_dir: Path):
        self.config_dir = config_dir
        self.channels_config = self._load_config("channels.yaml")
        self.quality_rules = self._load_config("quality-rules.yaml")

    def _load_config(self, filename: str) -> Dict:
        """加载配置文件"""
        config_path = self.config_dir / filename
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def get_channels_for_person(self, person_type: str) -> List[str]:
        """根据人物类型获取渠道列表（按优先级排序）"""
        person_config = self.channels_config['person_types'].get(person_type, {})
        priority_channels = person_config.get('priority_channels', [])

        # 获取所有启用的渠道
        all_channels = []
        for category, category_config in self.channels_config['channels'].items():
            for channel_name, channel_config in category_config.get('sub_channels', {}).items():
                if channel_config.get('enabled', False):
                    all_channels.append({
                        'name': channel_name,
                        'category': category,
                        'priority': channel_config.get('priority', 0)
                    })

        # 按优先级排序
        all_channels.sort(key=lambda x: x['priority'], reverse=True)

        # 优先返回人物类型指定的渠道
        result = []
        for channel_name in priority_channels:
            for channel in all_channels:
                if channel['name'] == channel_name:
                    result.append(channel)
                    break

        # 添加其他渠道
        for channel in all_channels:
            if channel not in result:
                result.append(channel)

        return result

    def search_channel(self, channel_name: str, person_name: str, keywords: List[str]) -> List[SearchResult]:
        """搜索单个渠道"""
        # 这里应该调用具体的渠道实现
        # 暂时返回空列表
        return []

    def search_all_channels(self, person_name: str, person_type: str) -> List[SearchResult]:
        """搜索所有渠道"""
        channels = self.get_channels_for_person(person_type)
        all_results = []

        for channel in channels:
            channel_name = channel['name']
            channel_config = self._get_channel_config(channel_name)

            if not channel_config:
                continue

            # 生成搜索关键词
            keywords = self._generate_keywords(channel_config, person_name)

            # 搜索
            try:
                results = self.search_channel(channel_name, person_name, keywords)
                all_results.extend(results)
            except Exception as e:
                print(f"渠道 {channel_name} 搜索失败: {e}")
                # 降级处理
                continue

        return all_results

    def _get_channel_config(self, channel_name: str) -> Optional[Dict]:
        """获取渠道配置"""
        for category, category_config in self.channels_config['channels'].items():
            if channel_name in category_config.get('sub_channels', {}):
                return category_config['sub_channels'][channel_name]
        return None

    def _generate_keywords(self, channel_config: Dict, person_name: str) -> List[str]:
        """生成搜索关键词"""
        keywords_template = channel_config.get('config', {}).get('search_keywords', [])
        return [kw.format(person_name=person_name) for kw in keywords_template]

    def is_blacklisted(self, url: str) -> bool:
        """检查URL是否在黑名单中"""
        blacklist = self.channels_config.get('blacklist', [])
        return any(domain in url for domain in blacklist)


# 使用示例
if __name__ == "__main__":
    config_dir = Path(__file__).parent.parent / "config"
    manager = ChannelManager(config_dir)

    # 获取中文人物的渠道
    channels = manager.get_channels_for_person("chinese_figure")
    print("中文人物渠道:")
    for channel in channels[:5]:
        print(f"  - {channel['name']} (优先级: {channel['priority']})")
