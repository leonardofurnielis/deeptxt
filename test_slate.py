# from spyder_index.embeddings import HuggingFaceEmbeddings

text = """
International Business Machines Corporation (using the trademark IBM), nicknamed Big Blue,[6] is an American multinational technology company headquartered in Armonk, New York and present in over 175 countries.[7][8] IBM is the largest industrial research organization in the world, with 19 research facilities across a dozen countries, having held the record for most annual U.S. patents generated by a business for 29 consecutive years from 1993 to 2021.[9][10][11]

IBM was founded in 1911 as the Computing-Tabulating-Recording Company (CTR), a holding company of manufacturers of record-keeping and measuring systems. It was renamed "International Business Machines" in 1924 and soon became the leading manufacturer of punch-card tabulating systems. During the 1960s and 1970s, the IBM mainframe, exemplified by the System/360, was the world's dominant computing platform, with the company producing 80 percent of computers in the U.S. and 70 percent of computers worldwide.[12]

IBM entered the microcomputer market in the 1980s with the IBM Personal Computer, which soon became known as PC, one of IBM's best selling products. Due to a lack of foresight by IBM,[13][14] the PC was not well protected by intellectual property laws. As a consequence, IBM quickly began losing its market dominance to emerging competitors in the PC market, while at the same time the openness of the PC platform has ensured PC's longevity as the most popular microcomputer standard.

Beginning in the 1990s, the company began downsizing its operations and divesting from commodity production, most notably selling its personal computer division to the Lenovo Group in 2005. IBM has since concentrated on computer services, software, supercomputers, and scientific research. Since 2000, its supercomputers have consistently ranked among the most powerful in the world, and in 2001 it became the first company to generate more than 3,000 patents in one year, beating this record in 2008 with over 4,000 patents.[12] As of 2022, the company held 150,000 patents.[15]

As one of the world's oldest and largest technology companies, IBM has been responsible for several technological innovations, including the automated teller machine (ATM), dynamic random-access memory (DRAM), the floppy disk, the hard disk drive, the magnetic stripe card, the relational database, the SQL programming language, and the UPC barcode. The company has made inroads in advanced computer chips, quantum computing, artificial intelligence, and data infrastructure.[16][17][18] IBM employees and alumni have won various recognitions for their scientific research and inventions, including six Nobel Prizes and six Turing Awards.[19]

IBM is a publicly traded company and one of 30 companies in the Dow Jones Industrial Average. It is among the world's largest employers, with over 297,900 employees worldwide in 2022.[20] Despite its relative decline within the technology sector,[21] IBM remains the seventh largest technology company by revenue, and 67th largest overall company by revenue in the United States. It is also consistently ranked among the world's most recognizable, valuable, and admired brands.[22]
"""

# embed_engine = HuggingFaceEmbeddings()

# text_embed = embed_engine.get_embedding_from_texts([text])

# print(text_embed)


# from spyder_index.core.document import Document
# from spyder_index.text_splitters.sentence import SentenceSplitter
# from spyder_index.text_splitters.semantic import SemanticSplitter

# doc = Document(text=text)

# splitter = SemanticSplitter()

# chunks = splitter.from_documents(documents=[doc])

# print(len(chunks))

#############  Test s3 reader

# from spyder_index.readers import S3Reader

# loader = S3Reader(bucket="spyder-bucket", 
#                      ibm_api_key_id="jq9JKjkrLfAEV9axrn2b7pE8eVm1excyRkqDQCEMNk-X", 
#                      ibm_service_instance_id="crn:v1:bluemix:public:cloud-object-storage:global:a/fe714114e937432ba4d4fa975d0f7e30:cff28c1b-bcb7-4e9e-8ddb-271b5109fdc4:bucket:spyder-bucket", 
#                      s3_endpoint_url="https://s3.br-sao.cloud-object-storage.appdomain.cloud")

# docs = loader.load_data()

# print(docs[0])
# print(len(docs))

#############  Test Spyder Json

from spyder_index.readers.file import JSONReader

loader = JSONReader(
    input_file='../data/DATIFIR com limit 100 199 ate Fim.json',
    jq_schema='.results[].body.view.value')

data = loader.load_data()

print(data[0])
print(len(data))

############  Test Spyder reader from directory

# from spyder_index.readers import DirectoryReader

# loader = DirectoryReader(input_dir='../data/')

# docs = loader.load_data()

# print(docs[0])
# print(len(docs))

#############  Test Spyder PDF from directory

# from spyder_index.readers.file import PDFReader

# loader = PDFReader(input_file='../data/My Estimate - AWS Pricing Calculator.pdf')

# docs = loader.load_data()

# print(docs[0])
# print(len(docs))
