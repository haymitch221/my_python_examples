# 来自 chenjiandongx/cutecharts 项目，尝试一下
from cutecharts.charts import Line


chart = Line("Demo-Line-chart")
# 设置chart的元数据
chart.set_options(
    labels=["12.01", "12.02", "12.03", "12.04", "12.05", "12.06", "12.07"], 
    x_label="I'm x-label", 
    y_label="I'm y-label",
)
# 设置数据
chart.add_series("series-A", [57, 134, 137, 129, 145, 60, 49])
chart.add_series("series-B", [114, 55, 27, 101, 125, 27, 105])
chart.render()
