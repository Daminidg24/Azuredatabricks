# Databricks notebook source
print("hello baby")

# COMMAND ----------

# MAGIC  %md
# MAGIC #Title1
# MAGIC ##title2
# MAGIC ###Tilrll3
# MAGIC text with a **bold** *italicized* in itand 
# MAGIC   ordered list
# MAGIC   1. once
# MAGIC   2. twice
# MAGIC   3. thrice
# MAGIC   unordered list
# MAGIC   *a
# MAGIC   *b
# MAGIC   *c
# MAGIC   *a
# MAGIC   *n
# MAGIC
# MAGIC   images:
# MAGIC   (https://www.bing.com/images/search?view=detailV2&ccid=HxV79tFM&id=F015C98E6E9DC4B26A1739DB459CACFE9D1EC242&thid=OIP.HxV79tFMPfBAIo0BBF-sOgHaEy&mediaurl=https%3a%2f%2fimages.pexels.com%2fphotos%2f443446%2fpexels-photo-443446.jpeg%3fcs%3dsrgb%26dl%3ddaylight-forest-glossy-443446.jpg%26fm%3djpg&exph=3403&expw=5266&q=images&simid=608032013786230371&FORM=IRPRST&ck=5C9EEE2E56E5079D3385F80316B3A874&selectedIndex=0)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

dbutils.fs.ls('/databricks-datasets/')

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets/')

# COMMAND ----------

print(files)

# COMMAND ----------

display(files)

# COMMAND ----------


