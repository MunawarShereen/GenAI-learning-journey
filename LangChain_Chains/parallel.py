from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel



load_dotenv()

HF_ToKEN = os.getenv("HF_TOKEN")
GEMINI_KEY = os.getenv("GEMINI_KEY")


llm1 = HuggingFaceEndpoint(
    repo_id = "google/gemma-2-2b-it",
    task = "text-generation",
)

model1 = ChatHuggingFace(llm=llm1)

llm2 = HuggingFaceEndpoint(
    repo_id = "google/gemma-2-2b-it",
    task = "text-generation",
)

model2 = ChatHuggingFace(llm=llm2)

prompt1 = PromptTemplate(
    template="Generate notes of  detailed report provided by the user {notes}.",
    input_variables=["notes"],
)

prompt2 = PromptTemplate(
    template="Generate a quiz from the notes {quiz}.",
    input_variables=["summary"],
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single document \n notes -> {notes}  and quiz -> {quiz}.",
    input_variables=["notes","quiz"],
)
parser = StrOutputParser()

parallel_chain = RunnableParallel(
    { "notes": prompt1 | model1 | parser, "quiz": prompt2 | model2 | parser }
)

chain = prompt3 | model1 | parser

reulted_chain = parallel_chain | chain

text = """
Pakistan: An Overview

Pakistan, officially the Islamic Republic of Pakistan, is a country located in South Asia, bordering India to the east, Afghanistan and Iran to the west, and China to the north. It also has a southern coastline along the Arabian Sea. With a population of over 240 million people, Pakistan is the fifth-most populous country in the world and home to diverse ethnic, linguistic, and cultural communities.

History

The history of Pakistan is rich and complex. The region has been home to some of the earliest human civilizations, including the Indus Valley Civilization, which flourished around 2500 BCE in what is now Sindh and Punjab provinces. Over centuries, the area saw the rise and fall of numerous empires, including the Persian Achaemenid Empire, Maurya Empire, Greco-Bactrian Kingdom, Mughal Empire, and Sikh Empire.

In 1947, following the end of British colonial rule in India, Pakistan was created as a separate homeland for Muslims under the leadership of Muhammad Ali Jinnah. Initially, it consisted of two regions: West Pakistan (modern-day Pakistan) and East Pakistan (modern-day Bangladesh), separated by about 1,600 kilometers of Indian territory. Tensions between the two wings led to the Bangladesh Liberation War in 1971, resulting in East Pakistan becoming the independent country of Bangladesh.

Geography

Pakistan’s geography is incredibly diverse. The north features mountain ranges like the Karakoram and the Himalayas, including K2, the second-highest peak in the world. Central Pakistan has fertile plains along the Indus River, which supports agriculture. The southern region includes the Baluchistan plateau and a coastline along the Arabian Sea. The country’s climate ranges from arid deserts in Sindh and Baluchistan to temperate zones in the northern mountains and humid regions along the coast.

Government and Politics

Pakistan is a federal parliamentary republic. The President is the ceremonial head of state, while the Prime Minister holds executive powers. The country has a bicameral legislature consisting of the National Assembly and the Senate. Pakistan has experienced periods of military rule interspersed with democratic governance. Its political system continues to evolve, with active debates over civil-military relations, judicial independence, and electoral reforms.

Economy

Pakistan has a mixed economy with significant agriculture, industry, and services sectors. Major agricultural products include wheat, rice, cotton, sugarcane, and fruits. Industrial production includes textiles, cement, steel, chemicals, and pharmaceuticals. Pakistan is also investing in technology and digital industries, with a growing IT outsourcing sector. The China-Pakistan Economic Corridor (CPEC) is a major infrastructure initiative connecting Gwadar Port to western China, enhancing trade and economic growth.

Culture and Society

Pakistani culture is diverse, reflecting centuries of historical influences. Languages include Urdu (the national language), Punjabi, Sindhi, Pashto, Balochi, and many regional dialects. Islam is the predominant religion, shaping traditions, festivals, and social norms. Pakistan is known for its music, poetry, and literature, including celebrated poets like Allama Iqbal and novelists like Mohsin Hamid.

Pakistani cuisine is famous worldwide, with dishes like biryani, nihari, kebabs, and samosas, and is influenced by Mughal, Persian, and regional traditions. Traditional clothing includes the shalwar kameez, worn by men and women alike.

Tourism and Landmarks

Pakistan has many natural and historical attractions:

Northern Areas: Hunza Valley, Skardu, Fairy Meadows, and Nanga Parbat.

Historic Sites: Mohenjo-daro (Indus Valley Civilization), Lahore Fort, Badshahi Mosque.

Cultural Sites: Faisal Mosque in Islamabad, ancient Buddhist ruins in Taxila.

Coastline and Desert: Clifton Beach in Karachi, Thar Desert in Sindh.

Challenges and Opportunities

Pakistan faces challenges such as political instability, energy shortages, water scarcity, and education gaps, but it also has enormous potential. With a young population, strategic location, and rich natural resources, Pakistan is poised for growth in technology, trade, and tourism. Efforts in renewable energy, urban development, and education reforms are shaping its future.

Conclusion

Pakistan is a country of contrasts — from towering mountains to vast deserts, ancient ruins to modern cities, and a rich tapestry of ethnic and linguistic diversity. Its history, culture, and strategic significance make it an important nation in South Asia, with a promising future shaped by its youth, resilience, and ambition.

"""

result = reulted_chain.invoke({"text": text})
print(result)

