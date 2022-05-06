from numpy.random import sample
import streamlit as st
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from PIL import Image

st.title("This is a title")
st.text('I am awesome')
st.markdown('Streamlit is ** really ** cool. :+1:')
st.markdown('# I am always awesome. :blush:')

st.header('Bu baslikmis.')
st.subheader('Bu da alt baslikmis.')

st.success('# I am successfull. :heart_eyes:')
st.info('## Yeter yahu, o kadar da super degilsin :stuck_out_tongue:')
st.error('### Aynen, bu ne hadsizlik, haddini bil :stuck_out_tongue_closed_eyes:')

st.help(range)

st.write('Hello world, :sunglasses:')

img = Image.open('image.jpeg')
st.image(img, caption='Bu bir resimdir', width=600)
st.image(img, caption='Bu bir resimdir', use_column_width=True)

my_video = open('video.mp4', 'rb')
st.video(my_video)
st.video('https://www.youtube.com/watch?v=fUXdrl9ch_Q')

cbox = st.checkbox('Hide/Show')
if cbox:
    st.write('Hello')
else:
    st.write('Good bye')

a = st.radio('Select a color:', ('White', 'Blue', 'Red', 'Purple'))
if a == 'Red':
    st.write('You chose red')
elif a == 'Purple':
    st.write('You chose purple')
else:
    st.write('You chose another color')

but = st.button('Predict')
if but:
    st.success('Basti')

sn = st.selectbox('Select a number', [1, 2, 3, 4, 5])

snn = st.selectbox('Select a function', range(10))
if snn == 2:
    st.info('Wooooov')

ms = st.multiselect('Select multiple numbers', range(10))
st.write(f'You selected {ms}.')

b = st.slider('Select', 1, 100, 50, 1)
st.write(f'You selected {b}.')

f = st.slider('Select', 0.5, 2.0, 1.0, 0.1)
# slider'da herhangi bir degeri float girersem tum degerleri float olarak yazmam gerekir
st.write(b * f)

# st.balloons()

st.date_input('Date', datetime.datetime.now())
st.time_input('Time', datetime.datetime.now())
st.time_input('Time2', datetime.time(12,0))
# burada sabit bir saat belirleyebiliyorum

st.code('import pandas as pd')
st.code('import numpy as np\nimport seaborn as sns')

with st.echo():
    import seaborn as sns
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    df = pd.DataFrame({'a':[1,2,3], 'b':[4,5,6]})
    df

st.sidebar.title('Sidebar title')
st.sidebar.markdown('## This is a markdown')
aa = st.sidebar.slider('input', 0,10,2,1)
# baslangic, bitis, default, kacar kacar
st.write('# sidebar input result')
st.success(aa * aa)

#dataframe
st.write("# dataframes")
df = pd.read_csv("final_scout_dummy.csv", nrows=(100))
st.table(df.head()) #dynamic degil 
st.write(df.head()) #dynamic, you can sort, swiss knife
st.dataframe(df.head())#dynamic

#charts
st.write("# age")
st.line_chart(df.age)

st.write("# sidebar select") #double click to reset
x=st.sidebar.slider("line chart input")
srs = pd.Series(np.random.randn(x))
st.line_chart(srs)

# with st.echo():
#     import seaborn as sns
#     penguins = sns.load_dataset("penguins")
#     st.title("Hello")
#     fig = sns.pairplot(penguins, hue="species")
#     st.pyplot(fig)

# Proje ornegi
# split the data into train and test

from sklearn.model_selection import train_test_split
import pickle
# to build linear regression_model
from sklearn.linear_model import LinearRegression

with st.echo():
    df = pd.read_csv("Advertising.csv")
    X= df.drop("sales", axis=1)
    y= df["sales"]
    x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)
    model = LinearRegression()
    model.fit(x_train, y_train)
    filename = 'finalized_model.sav'
    pickle.dump(model, open(filename, 'wb'))
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.score(x_test, y_test)
    st.write(result)
    pred = model.predict([[100,200,300]])
    st.write(pred)

st.table(df.head())
a = float(st.sidebar.number_input("TV:",value=230.1, step=10.1))
b = float(st.sidebar.number_input("radio:",value=37.8, step=10.1))
c = float(st.sidebar.number_input("newspaper:",value=69.2, step=10.1))
if st.button("Predictt"): 
    pred = model.predict([[a,b,c]])
    st.write(pred)

#NLP-example

#NLP-example

#data = ["I love you", "I hate you"],
txt = st.text_area("Enter a message", "I love you",20,150)
from transformers import pipeline
if st.button("Analyze"):
    st.success("analyzing")
    sentiment_pipeline = pipeline("text-classification")
    st.write(sentiment_pipeline(txt))

st.write('Ben buradayim.')