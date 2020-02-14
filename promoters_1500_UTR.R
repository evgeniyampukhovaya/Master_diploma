setwd('C:/Users/puhovajaem/Работа/FUS3_new_data/motif_to_PWM_and_threshold')
annotation_gff <- read.delim('Araport11_GFF3_genes_transposons.201606.gff', header = F, stringsAsFactors = F)
annotation_gff_genes <- annotation_gff[annotation_gff$V3 == 'gene',]
annotation_gff_genes_protein_cod <- annotation_gff_genes[grep('locus_type=protein_coding', annotation_gff_genes$V9),]
annotation_gff_genes_protein_cod$prom_start[annotation_gff_genes_protein_cod$V7 == '+'] <- annotation_gff_genes_protein_cod$V4[annotation_gff_genes_protein_cod$V7 == '+'] - 1500
annotation_gff_genes_protein_cod$prom_end[annotation_gff_genes_protein_cod$V7 == '-'] <- annotation_gff_genes_protein_cod$V5[annotation_gff_genes_protein_cod$V7 == '-'] + 1500
library(stringr)
for (i in 1:nrow(annotation_gff_genes_protein_cod)) {
  annotation_gff_genes_protein_cod$Name[i] <-
    substr(annotation_gff_genes_protein_cod$V9[i], 4, 12)
}

# добавить утр


annotation_5utr <- annotation_gff[annotation_gff$V3 == 'five_prime_UTR',]

for (i in 1:nrow(annotation_5utr)) {
  annotation_5utr$Name[i] <-
    substr(annotation_5utr$V9[i], 4, 12)
}

for (i in 1:nrow(annotation_gff_genes_protein_cod)) {
  utr_subset <- annotation_5utr[annotation_5utr$Name == annotation_gff_genes_protein_cod$Name[i],]
  if (length(utr_subset$V1) > 0){
  utr <- ifelse(annotation_5utr$V7[i] == '+', max(utr_subset$V5), min(utr_subset$V4))
} else utr <- NA
annotation_gff_genes_protein_cod$UTR[i] <- utr
}

annotation_gff_genes_protein_cod$prom_end[(annotation_gff_genes_protein_cod$V7 == '+')&(is.na(annotation_gff_genes_protein_cod$UTR))] <- annotation_gff_genes_protein_cod$V4[(annotation_gff_genes_protein_cod$V7 == '+')&(is.na(annotation_gff_genes_protein_cod$UTR))]

annotation_gff_genes_protein_cod$prom_end[(annotation_gff_genes_protein_cod$V7 == '+')&(!(is.na(annotation_gff_genes_protein_cod$UTR)))] <- annotation_gff_genes_protein_cod$UTR[(annotation_gff_genes_protein_cod$V7 == '+')&(!(is.na(annotation_gff_genes_protein_cod$UTR)))]



annotation_gff_genes_protein_cod$prom_start[(annotation_gff_genes_protein_cod$V7 == '-')&(is.na(annotation_gff_genes_protein_cod$UTR))] <- annotation_gff_genes_protein_cod$V5[(annotation_gff_genes_protein_cod$V7 == '-')&(is.na(annotation_gff_genes_protein_cod$UTR))]

annotation_gff_genes_protein_cod$prom_start[(annotation_gff_genes_protein_cod$V7 == '-')&((!is.na(annotation_gff_genes_protein_cod$UTR)))] <- annotation_gff_genes_protein_cod$UTR[(annotation_gff_genes_protein_cod$V7 == '-')&(!(is.na(annotation_gff_genes_protein_cod$UTR)))]



promoters_with_utr <- annotation_gff_genes_protein_cod[,c(1,10,11,12,7)]
promoters_with_utr$V1 <- gsub('Chr', '', promoters_with_utr$V1)
promoters_with_utr <- promoters_with_utr[promoters_with_utr$V1 != 'C',]
promoters_with_utr <- promoters_with_utr[promoters_with_utr$V1 != 'M',]
write.table(promoters_with_utr, 'Araport11_201606_prot_cod_gene_promoters_1500_longest_UTR_strain.bed', row.names = F, col.names = F, sep = '\t', quote = F)

















# x <- annotation_5utr[grep('AT1G01060', annotation_5utr$V9),]# 
# max(grep('AT1G01060', annotation_5utr$V9))
# grep(gene_list_annotation_without_rnas$Name[3],annotation_5utr$V9)

# for (i in 1:nrow(annotation_gff_genes_protein_cod)){
#   annotation_gff_genes_protein_cod$UTR[i] <- ifelse(annotation_gff_genes_protein_cod$V7[i] == '+',annotation_5utr$V5[max(grep(annotation_gff_genes_protein_cod$Name[i],annotation_5utr$V9))], annotation_5utr$V4[max(grep(annotation_gff_genes_protein_cod$Name[i],annotation_5utr$V9))] )
#   
# }


# for (i in 1:nrow(gene_list_annotation_without_rnas)){
#   if (is.na(gene_list_annotation_without_rnas$UTR[i])){
#     gene_list_annotation_without_rnas$promoter_Lena_start[i] <- gene_list_annotation_without_rnas$promoter_start[i]
#     gene_list_annotation_without_rnas$promoter_Lena_end[i] <- gene_list_annotation_without_rnas$promoter_end[i]
#   }
#   else{
#     if (gene_list_annotation_without_rnas$strand[i] == '+'){
#     gene_list_annotation_without_rnas$promoter_Lena_start[i] <- gene_list_annotation_without_rnas$promoter_start[i]
#     gene_list_annotation_without_rnas$promoter_Lena_end[i] <- gene_list_annotation_without_rnas$UTR[i]
#   }
#     else if (gene_list_annotation_without_rnas$strand[i] == '-'){
#       gene_list_annotation_without_rnas$promoter_Lena_start[i] <- gene_list_annotation_without_rnas$UTR[i]
#       gene_list_annotation_without_rnas$promoter_Lena_end[i] <- gene_list_annotation_without_rnas$promoter_end[i]
#     }
# }





