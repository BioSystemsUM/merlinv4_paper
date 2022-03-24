# Merlin paper

### Table of contents:

- [Requirements](#requirements)
- [Sequences](#sequences)
- [Tools models](#tools-models)
- [Merlin models](#merlin-models)
  - [Automatic workflow](#automatic-workflow)
  - [SamPler](#sampler)
  - [Workspaces](#workspaces)
- [Reactions identifier conversion](#reactions-identifier-conversion)
- [Assessment](#assessment)

## Requirements

## Sequences

The gene sequences used to reconstruct each of the Genome-Scale Metabolic Models (GSMM) are stored in the folder "Sequences".
The files are in FASTA and GFF format. 
The FASTA file of the gene sequences used for AuReMe template models were preprocessed to include only the locus tag. 
The preprocessing scripts and resultant FASTA files are stored in the "Template models genomes processing" folder.
This preprocess will convert a file from this: 

```text
>lcl|NC_000913.3_prot_NP_414544.1_3 [gene=thrB] [locus_tag=b0003] [db_xref=UniProtKB/Swiss-Prot:P00547] [protein=homoserine kinase] [protein_id=NP_414544.1] [location=2801..3733] [gbkey=CDS]
MVKVYAPASSANMSVGFDVLGAAVTPVDGALLGDVVTVEAAETFSLNNLGRFADKLPSEPRENIVYQCWE
RFCQELGKQIPVAMTLEKNMPIGSGLGSSACSVVAALMAMNEHCGKPLNDTRLLALMGELEGRISGSIHY
DNVAPCFLGGMQLMIEENDIISQQVPGFDEWLWVLAYPGIKVSTAEARAILPAQYRRQDCIAHGRHLAGF
IHACYSRQPELAAKLMKDVIAEPYRERLLPGFRQARQAVAEIGAVASGISGSGPTLFALCDKPETAQRVA
DWLGKNYLQNQEGFVHICRLDTAGARVLEN
```

to this:

```text
>b0003
MVKVYAPASSANMSVGFDVLGAAVTPVDGALLGDVVTVEAAETFSLNNLGRFADKLPSEPRENIVYQCWE
RFCQELGKQIPVAMTLEKNMPIGSGLGSSACSVVAALMAMNEHCGKPLNDTRLLALMGELEGRISGSIHY
DNVAPCFLGGMQLMIEENDIISQQVPGFDEWLWVLAYPGIKVSTAEARAILPAQYRRQDCIAHGRHLAGF
IHACYSRQPELAAKLMKDVIAEPYRERLLPGFRQARQAVAEIGAVASGISGSGPTLFALCDKPETAQRVA
DWLGKNYLQNQEGFVHICRLDTAGARVLEN
```

This conversion is performed so that AuReMe could map the locus tag of each gene to the genes found in the template GSMM.


## Tools models

Each draft and curated model is stored in the "Models" folder.
