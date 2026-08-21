# Clinic Mobile

悦舒运动康复管理系统的 Android WebView 客户端（纯壳应用，无本地网页资源）。

移动端网页部署在服务器 `https://66.154.101.204/mobile/`，源码由
`clinic-business-fix` 仓库的 `mobile/` 目录维护；本仓库只负责打包 Android APK。

## APK 构建

推送到 `main` 分支后，GitHub Actions 的 **Build Android APK** 工作流会自动构建并验证可安装 APK。
完成后可在该次运行的 Artifacts 中下载 `clinic-mobile-apk`。

也可以在 Actions 页面手动运行 `workflow_dispatch`。

APK 默认打开：`https://66.154.101.204/mobile/`
