"""
@authors: Juan L. Trincado
@email: juanluis.trincado@upf.edu
IR_ePydoor.py: get significat exonizations
"""

import os

from lib.IR.extract_significant_IR import *
from lib.IR.IR_associate_gene_ids import *
from lib.IR.filter_IR import *
from lib.IR.filter_IR_CHESS import *
from lib.IR.generate_random_intronic_positions import *
from lib.IR.get_coverageBed import *
from lib.IR.get_coverageBed_adapter import *
from lib.IR.get_peptide_sequence_RI import *
from lib.IR.select_fasta_candidates import *
from lib.IR.run_netMHC_classI_slurm_part1 import *
from lib.IR.run_netMHC_classI_slurm_part2 import *
from lib.IR.run_netMHCpan_classI_slurm_part1 import *
from lib.IR.run_netMHCpan_classI_slurm_part2 import *
from lib.IR.format_to_SPADA import *

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create console handler and set level to info
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


def main():
    try:

        logger.info("Starting execution")

        HLAclass_path = "/homes/users/jtrincado/scratch/test_Junckey/PHLAT_summary_ClassI_all_samples.out"
        HLAtypes_path = "/homes/users/jtrincado/scratch/test_Junckey/NetMHC-4.0_HLA_types_accepted.tab"
        HLAtypes_pan_path = "/homes/users/jtrincado/scratch/test_Junckey/NetMHCpan-4.0_HLA_types_accepted.tab"
        netMHC_path = "/homes/users/jtrincado/scratch/Software/netMHC-4.0/netMHC"
        netMHC_pan_path = "/homes/users/jtrincado/scratch/Software/netMHCpan-4.0/netMHCpan"
        output_path = "/homes/users/jtrincado/scratch/test_Junckey/test2"

        #13. Run netMHC-4.0_part2
        logger.info("Part13...")
        run_netMHC_classI_slurm_part2(output_path + "/IR_ORF_filtered_peptide_change.tab", HLAclass_path, HLAtypes_path,
                                      output_path + "/IR_fasta_files",output_path + "/IR_NetMHC-4.0_files", output_path + "/IR_NetMHC-4.0_neoantigens_type_3.tab",
                                      output_path + "/IR_NetMHC-4.0_neoantigens_type_3_all.tab", output_path + "/IR_NetMHC-4.0_neoantigens_type_2.tab",
                                      output_path + "/IR_NetMHC-4.0_neoantigens_type_2_all.tab", output_path + "/IR_NetMHC-4.0_junctions_ORF_neoantigens.tab",
                                      netMHC_path)

        #14. Run netMHCpan-4.0_part2
        logger.info("Part14...")
        run_netMHCpan_classI_slurm_part2(output_path + "/IR_ORF_filtered_peptide_change.tab", HLAclass_path, HLAtypes_pan_path,
                                      output_path + "/IR_fasta_files",output_path + "/IR_NetMHCpan-4.0_files", output_path + "/IR_NetMHCpan-4.0_neoantigens_type_3.tab",
                                      output_path + "/IR_NetMHCpan-4.0_neoantigens_type_3_all.tab", output_path + "/IR_NetMHCpan-4.0_neoantigens_type_2.tab",
                                      output_path + "/IR_NetMHCpan-4.0_neoantigens_type_2_all.tab", output_path + "/IR_NetMHCpan-4.0_junctions_ORF_neoantigens.tab",
                                      netMHC_pan_path)

        # 15. Run format_to_SPADA
        logger.info("Part15...")
        format_to_SPADA(output_path + "/IR_ORF.tab", output_path + "/IR_ORF_sequences.tab", output_path + "/IR_ORF_Interpro.tab",
                        output_path + "/IR_ORF_IUPred.tab", output_path + "/IR_SPADA.tab", output_path + "/IR_SPADA.fasta",
                        output_path + "/IR_SPADA_features.tab")

        logger.info("Done.")

        exit(0)

    except Exception as error:
        logger.error('ERROR: ' + repr(error))
        logger.error("Aborting execution")
        sys.exit(1)


if __name__ == '__main__':
    main()