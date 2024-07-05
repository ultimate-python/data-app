import streamlit as st
import pandas as pd

#เขียนข้อความลงเวป
st.title('Web App วิเคราะห์การทำงาน')

#อ่านข้อมูลจากไฟล์ csv เพื่อไปใช้บนเวป
data_df = pd.read_csv('training_task_tickets_final.csv')

#นำข้อมูลที่อ่านจากไฟล์ มาแสดงเป็นตารางบนเวป
st.write('ตารางข้อมูลทั้งหมดของการทำงานจากสัปดาห์ที่ผ่านมา')
st.dataframe(data_df)

#สร้าง columns 4 คอลัมน์
st.write('จำนวนงานแบ่งตามสถานะ')
col1, col2, col3, col4 = st.columns(4)

#นำข้อมูลใส่ col1
pending_df = data_df[data_df['Status'] == '1 รอดำเนินการ']
col1.metric('1 รอดำเนินการ',len(pending_df))

#นำข้อมูลใส่ col2
processa_df = data_df[data_df['Status'] == '2 ขั้นตอน A']
col2.metric('2 ขั้นตอน A',len(processa_df))

#นำข้อมูลใส่ col3
processb_df = data_df[data_df['Status'] == '3 ขั้นตอน B']
col3.metric('3 ขั้นตอน B',len(processb_df))

#นำข้อมูลใส่ col4
finish_df = data_df[data_df['Status'] == '4 เสร็จสิ้น']
col4.metric('4 เสร็จสิ้น',len(finish_df))

#การนับจำนวนตามกลุ่มข้อมูล
pic_df = data_df.groupby(['PIC','Status']).count()['Task Name'].reset_index()
#st.dataframe(pic_df)
st.write('งานแบ่งตามผู้รับผิดชอบ และสถานะล่าสุด')
st.bar_chart(pic_df,x='PIC',y='Task Name',color='Status')