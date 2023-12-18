# scripts/your_script.py
import seqspec_parse.process as process

file_path = "/Users/ericche/Downloads/QC/notebooks/bulk/anbe_reporter_spec/anbe_reporter_spec_081423.yaml"

R1 = process.R1(file_path, barcode_tag = "R1_barcode", spacer_tag = "spacer", hamming_distance = 2)
print(R1)
print(R1 == "'^(?P<cell_1>.{3,9})(?P<discard_1>GGAAAGGACGAAACACCG){s<=2}(?P<guide_1>.{20})(?P<discard_2>.+)$'")

R2 = process.R2(file_path, barcode_tag = "R2_barcode", reporter_tag = "reporter")
print(R2)
print(R2 == "'^(?P<umi_1>.{4})(?P<surrogate_1>.{32})(?P<discard_1>.+)$'")