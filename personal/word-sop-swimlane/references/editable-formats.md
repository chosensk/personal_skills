# 可编辑格式与验证

## 共用模型

先建立与格式无关的数据：`lanes`、`stages`、`nodes`、`edges`。节点记录 `id`、`lane`、`stage`、`title`、`actions`、`system_path`、`controls`、`evidence_blocks`、`image_ids`、`responsibility_status`；边记录源节点、目标节点及是否待补。根据截图原始比例计算节点高度，再取同一阶段各泳道所需高度的最大值。实际节点与阶段数量来自文档，不硬编码销售管理案例。

## drawio

生成UTF-8 mxfile / diagram / mxGraphModel / root结构，包含id=0和parent=0的id=1基础cell。每个节点为可编辑的mxCell；文字与图片可以作为节点的子cell，使移动节点时跟随。图片使用 `shape=image;imageAspect=0;aspect=fixed;image=data:image/png,<base64>;`（drawio这种image值无 `;base64` 标记），mxGeometry存储位置与尺寸。保留图内独立节点和source/target连接，不能仅嵌入完整SVG截图。几何与连线用同一份模型生成，避免预览图与源文件流程不一致。

## VSDX

用户要求WPS导入VSDX时，优先使用当前环境已验证的生成器或合法模板。没有生成能力时如实交付drawio，不把SVG/ZIP改后缀伪装成VSDX。不将含内部数据的文件上传到外部转换服务。

若直接写OOXML包：使用Visio 2012 namespace，保留有效的document、styles、pages及其package relationships。PageWidth/PageHeight匹配画布；坐标转换注意Visio的Y轴方向。Shape子元素顺序为Cell、Section、Text或ForeignData等，不能将Cell写到Text后面。

- 图片Shape使用 `Type="Foreign"`，具有Pin、Width、Height、LocPin和ImgWidth/ImgHeight等尺寸Cell。
- `ForeignData ForeignType="Bitmap" CompressionType="PNG"` 内的Rel通过 `r:id` 引用page关系，目标为 `../media/<image>.png`。
- 图片字节写入 `visio/media/`，在Content_Types中声明PNG MIME类型。
- 普通形状、文字与连线保持原生对象；连接关系绑定实际节点，而不只绘制静态箭头。
- 图片与节点若未建立分组，交付说明须提示移动节点时同时选择图片。不能宣称未实现的跟随行为。
- 不把生成SVG预览成功或XML校验成功描述为实际WPS导入成功。

## 预览与校验

SVG图片使用 `data:image/png;base64,...` 自包含URI。以依赖工具返回的Node与sharp渲染PNG，适当设置大画布限制，保留截图原始字节；阶段裁切保留岗位列头。所有阶段都应查看，完整图核查跨阶段连线。

结构校验至少包括：所有节点ID唯一、连线端点存在、节点不越所属阶段、各图片引用有效、VSDX所有非外部relationship目标在ZIP中存在、每份嵌入图片的SHA256与提取图片一致。保留图片映射与待确认项说明即可，无需把分析日志全部交付。
