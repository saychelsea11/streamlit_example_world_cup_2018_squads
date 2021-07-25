import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams.update(plt.rcParamsDefault)
plt.style.use('bmh')
fig3 = plt.figure(constrained_layout=True,figsize=(21,11))
gs = fig3.add_gridspec(40,40)

#Markdown text using Streamlit's 'write' function
st.write("""
# Analyzing FIFA World Cup 2018 Squads
""")s

#Plotting using streamlit's 'pyplot' function
df = pd.read_csv("world_cup_2018_squads.csv",encoding='iso-8859-1')

st.write("""### 1. Data overview""",df.head())

st.write("""### 2. *Caps* and *goals*""")

#The following methods for defining 'fig' also work for the pyplot function
#fig, ax = plt.subplots()
#fig = plt.figure()

fig3.add_subplot(gs[0:19,0:20])
plt.hist(df['Caps'],range=(0,160),bins=16,alpha=0.8)
plt.ylabel('Frequency',fontsize=25)
plt.xlabel('Caps',fontsize=25)
plt.xticks(size=20)
plt.yticks(size=20)

fig3.add_subplot(gs[21:,0:20])
plt.hist(df['Goals'],range=(0,80),bins=16,alpha=0.8,color='brown')
plt.ylabel('Frequency',fontsize=25)
plt.xlabel('Goals',fontsize=25)
plt.xticks(size=20)
plt.yticks(size=20)

fig3.add_subplot(gs[0:19,20:])
plt.scatter(range(len(df['Caps'])),df['Caps'],alpha=0.8)
plt.ylabel('Caps',fontsize=25)
plt.xlabel('Player',fontsize=25)
plt.xticks(size=20)
plt.yticks(size=20)

fig3.add_subplot(gs[21:,20:])
plt.scatter(range(len(df['Goals'])),df['Goals'],alpha=0.8,color='brown')
plt.ylabel('Goals',fontsize=25)
plt.xlabel('Player',fontsize=25)
plt.xticks(size=20)
plt.yticks(size=20)

st.pyplot(fig3)

st.write("""
### 3. *Positions*
""")

plt.rcParams.update(plt.rcParamsDefault)
plt.style.use('bmh')
fig4 = plt.figure(constrained_layout=True,figsize=(21,11))
gs = fig4.add_gridspec(40,40)

sns.countplot(data=df,x='Position',alpha=0.8)
plt.xticks(size=20)
plt.yticks(size=20)
plt.ylabel('Frequency',fontsize=25)
plt.xlabel('Position',fontsize=25)

st.pyplot(fig4)

#Another plotting option with streamlit's 'line_chart' function
#st.line_chart(df['Caps'])