# 配置指南

## 快速开始

### 1. Fork 或克隆仓库

```bash
git clone https://github.com/J1ezds/some-star.git
cd some-star
```

### 2. 配置 GitHub Token

#### 方式一：使用 GitHub Actions（推荐）

仓库已配置好 workflow，使用默认的 `GITHUB_TOKEN` 即可运行。

如需使用 Personal Access Token（PAT），可添加为仓库密钥：

1. 进入仓库 → Settings → Secrets and variables → Actions
2. 点击 "New repository secret"
3. 名称：`MY_TOKEN`
4. 值：你的 PAT token
5. 修改 `.github/workflows/sync.yml`：

```yaml
- run: python sync_stars.py
  env:
    GH_TOKEN: ${{ secrets.MY_TOKEN }}
```

#### 方式二：本地运行

```bash
export GH_TOKEN="your_token_here"
python sync_stars.py
```

### 3. 修改用户名

编辑 `sync_stars.py` 第 6 行：

```python
USERNAME = "你的GitHub用户名"
```

---

## 配置项说明

### sync_stars.py

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `USERNAME` | GitHub 用户名 | `J1ezds` |
| `GH_TOKEN` | 认证 token | 环境变量 |

### .github/workflows/sync.yml

| 配置 | 说明 | 默认值 |
|------|------|--------|
| `cron` | 定时表达式 | `0 0 * * *`（每天 UTC 0 点） |
| `workflow_dispatch` | 手动触发 | 已启用 |

---

## 定时表达式示例

```yaml
schedule:
  - cron: '0 0 * * *'    # 每天 UTC 0 点
  - cron: '0 */6 * * *'  # 每 6 小时
  - cron: '0 0 * * 1'    # 每周一
  - cron: '0 0 1 * *'    # 每月 1 号
```

---

## 本地开发

### 安装依赖

```bash
pip install requests
```

### 运行脚本

```bash
python sync_stars.py
```

生成的 `README.md` 会自动更新。

---

## 常见问题

### Q: 如何更改同步频率？

修改 `.github/workflows/sync.yml` 中的 `cron` 表达式。

### Q: Token 权限不足？

确保 PAT 有 `repo` 和 `read:user` 权限。

### Q: 如何排除某些语言？

修改 `sync_stars.py` 中的 `categorize_by_language` 函数，添加过滤逻辑。

### Q: 生成的 README 格式如何自定义？

修改 `generate_readme` 函数中的模板。
