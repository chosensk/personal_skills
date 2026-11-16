# 可编辑格式与验证

## 共用模型

先建立与格式无关的数据：`nodes`、`edges`，以及适用时的 `lanes`、`stages`。节点记录 `id`、`title`、`actions` 和来源；根据材料补充 `lane`、`stage`、`system_path`、`controls`、`image_ids`、`responsibility_status`。边记录源节点、目标节点、分支条件及是否待补。存在截图时按原始比例计算节点尺寸；存在泳道阶段时取同一阶段各泳道所需高度的最大值。图型、节点及阶段数量来自任务，不硬编码案例。

## drawio

生成UTF-8 mxfile / diagram / mxGraphModel / root结构，包含id=0和parent=0的id=1基础cell。每个节点为可编辑的mxCell；文字与图片可以作为节点的子cell，使移动节点时跟随。图片用 `shape=image;imageAspect=0;aspect=fixed` 和匹配原始格式的data URI嵌入，例如PNG用 `image=data:image/png,<base64>;`，JPEG用 `image=data:image/jpeg,<base64>;`（drawio这种image值无 `;base64` 标记）；mxGeometry存储位置与尺寸。保留图内独立节点和source/target连接，不能仅嵌入完整SVG截图。几何与连线用同一份模型生成，避免预览图与源文件流程不一致。

## VSDX

用户要求VSDX时，优先使用当前环境已验证的生成器或合法模板。没有生成能力时如实交付drawio并说明VSDX未生成，不把SVG/ZIP改后缀伪装成VSDX。不将含内部数据的文件上传到外部转换服务。

若直接写OOXML包：使用Visio 2012 namespace，保留有效的document、styles、pages及其package relationships。PageWidth/PageHeight匹配画布；坐标转换注意Visio的Y轴方向。Shape子元素顺序为Cell、Section、Text或ForeignData等，不能将Cell写到Text后面。

- 图片Shape使用 `Type="Foreign"`，具有Pin、Width、Height、LocPin和ImgWidth/ImgHeight等尺寸Cell。
- `ForeignData ForeignType="Bitmap" CompressionType="PNG"` 内的Rel通过 `r:id` 引用page关系，目标为 `../media/<image>.png`。
- 图片字节写入 `visio/media/`，在Content_Types中声明PNG MIME类型。
- 普通形状、文字与连线保持原生对象；连接关系绑定实际节点，而不只绘制静态箭头。
- 图片与节点若未建立分组，交付说明须提示移动节点时同时选择图片。不能宣称未实现的跟随行为。
- 不把生成SVG预览成功或XML校验成功描述为实际WPS导入成功。

## 预览与校验

有嵌入截图时，SVG图片使用与原始格式匹配的自包含data URI。需要PNG时可用依赖工具返回的Node与sharp渲染，适当设置大画布限制；泳道阶段裁切保留岗位列头。查看完整图和所有已生成分图，核查跨阶段连线。

结构校验至少包括所有节点ID唯一、连线端点存在；有阶段时检查节点不越所属阶段，有图片时检查引用及来源映射，有VSDX时检查所有非外部relationship目标在ZIP中存在。优先保留图片原始字节并比较嵌入内容与来源的SHA256；格式不支持而必须转换时，保留来源与转换后文件的映射及各自哈希，核查尺寸比例、内容与标注，说明转换，不能声称字节一致。保留适用的图片映射与待确认项说明，无需把分析日志全部交付。
