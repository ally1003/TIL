# Comparison with SQL



```python
import pymysql.cursors
import pandas as pd

sql="select customers.state, customers.customerName, payments.checkNumber from customers LEFT JOIN payments on customers.customerNumber = payments.customerNumber where payments.paymentDate >= '2004-10-06';"

conn = pymysql.connect(host='localhost', user='me', 
                       password='******', db='classicmodels', charset='utf8',
                       autocommit=True, cursorclass=pymysql.cursors.DictCursor)
try:

   with conn.cursor() as curs:
      curs.execute(sql)
      rs = curs.fetchall()

      # DB에서 받아온 값을 DataFrame에 넣음

      df = pd.DataFrame(rs)
      print(df)
    
    #df.to_csv('query.csv')

finally:

   conn.close()
```



## GROUP BY

In pandas, SQL’s GROUP BY operations are performed using the similarly named [`groupby()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby) method.

```sql
SELECT sex, count(*)
FROM tips
GROUP BY sex;
```



```python
tips.groupby("sex").size()
```



## JOIN

JOINs can be performed with [`join()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html#pandas.DataFrame.join) or [`merge()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html#pandas.merge). By default, [`join()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html#pandas.DataFrame.join) will join the DataFrames on their indices.

```python
df1 = pd.DataFrame({"key": ["A", "B", "C", "D"], "value": np.random.randn(4)})
```





---

교과:  SQL로 맛보는 데이터 전처리 분석

진도:  2장 SQL문법



유요한 참고 링크

https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html#compare-with-sql