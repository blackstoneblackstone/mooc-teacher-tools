# PPT Watermark and PDF Conversion

本项目用于在 PPT 文件上添加水印，并将带有水印的 PPT 转换为 PDF。

## 安装

1. 确保您已安装 Python 3。
2. 克隆此仓库或将其下载为 ZIP 文件。
3. 在项目根目录下运行以下命令以安装依赖项：`pip3 install -r requirements.txt` 


## 使用方法

1. 将输入的 PPT 文件（如 `input.pptx`）和水印图片（如 `watermark.png`）放到 `assets` 的 `input` 文件夹中。
2. 修改代码中的 `input_ppt`、`watermark_image`、`output_ppt` 和 `output_pdf` 变量，以指向正确的文件路径（如果需要）。
3. 运行 `main.py` 文件： `python main.py`
4. 生成的带有水印的 PPT 文件将保存为 `output.pptx`（在 `assets` 文件夹中），生成的 PDF 文件将保存为 `output.pdf`（在 `assets` 文件夹中）。

## 注意事项

- 本项目使用 [python-pptx](https://github.com/scanny/python-pptx)，[Pillow](https://pillow.readthedocs.io/en/stable/) 和 [Aspose.Slides for Python](https://docs.aspose.com/slides/) 库。
- Aspose Slides 是一个收费的插件，所以生成的 PDF 会有一个水印，需要手动删除了。
- 水印图片建议使用透明背景，以便更好地融合到 PPT 中。
- 请确保您的 PPT 文件格式为 `.pptx`，因为本项目仅支持此格式。
