/*
A KBase module for interacting with Metagenomic data in KBase
*/
module MetagenomeUtils {

    /* 
      An X/Y/Z style reference
    */
    typedef string obj_ref;

    /* A boolean - 0 for false, 1 for true.
        @range (0, 1)
    */
    typedef int boolean;

    /*
      file_directory: file directory containing compressed/unpacked contig file(s) to build BinnedContig object
      assembly_ref: Metagenome assembly object reference
      binned_contig_name: BinnedContig object name
      workspace_name: the name/id of the workspace it gets saved to
    */
    typedef structure {
      string file_directory;
      obj_ref assembly_ref;
      string binned_contig_name;
      string workspace_name;
    } FileToBinnedContigParams;

    typedef structure {
      obj_ref binned_contig_obj_ref;
    } FileToBinnedContigResult;

    /*
      file_to_binned_contigs: Generating BinnedContigs ojbect from files

      input params:
      file_directory: file directory containing compressed/unpacked contig file(s) to build BinnedContig object
      assembly_ref: Metagenome assembly object reference
      binned_contig_name: BinnedContig object name
      workspace_name: the name/id of the workspace it gets saved to

      return params:
      binned_contig_obj_ref: generated result BinnedContig object reference

    */
    funcdef file_to_binned_contigs(FileToBinnedContigParams params)
        returns (FileToBinnedContigResult returnVal) authentication required;

    /*
      input_ref: BinnedContig object reference

      optional params:
      not_save_to_shock: not saving result bin files to shock
    */
    typedef structure {
      string input_ref;
      boolean not_save_to_shock;
    } ExportParams;

    /*
      shock_id: saved packed file shock id
      bin_file_list: a list of bin file path
    */
    typedef structure {
      string shock_id;
      list <string> bin_file_list;
    } ExportOutput;

    /*
      binned_contigs_to_file: Convert BinnedContig object to fasta files and pack them to shock

      required params:
      input_ref: BinnedContig object reference

      optional params:
      not_save_to_shock: not saving result bin files to shock

      return params:
      shock_id: saved packed file shock id (None if not_save_to_shock is set)
      bin_file_list: a list of bin file path
    */
    funcdef binned_contigs_to_file(ExportParams params)
        returns (ExportOutput returnVal) authentication required;

    /*
      binned_contig_obj_ref: BinnedContig object reference
      extracted_assemblies: a list of:
            bin_id: target bin id to be extracted
            output_assembly_name: output assembly object name
      workspace_name: the name of the workspace it gets saved to
    */
    typedef structure {
      obj_ref binned_contig_obj_ref;
      string bin_id;
      string output_assembly_name;
      list<mapping<string, string>> extracted_assemblies;
      string workspace_name;
    } ExtractBinAsAssemblyParams;

    /*
      assembly_ref_list: list of generated Assembly object reference
      report_name: report name generated by KBaseReport
      report_ref: report reference generated by KBaseReport
    */
    typedef structure {
      list <obj_ref> assembly_ref_list;
      string report_name;
      string report_ref;
    } ExtractBinAsAssemblyResult;

    /*
      extract_binned_contigs_as_assembly: extract one/multiple Bins from BinnedContigs as Assembly object

      input params:
      binned_contig_obj_ref: BinnedContig object reference
      extracted_assemblies: a list of:
            bin_id: target bin id to be extracted
            output_assembly_name: output assembly object name
      workspace_name: the name of the workspace it gets saved to

      return params:
      assembly_ref_list: list of generated result Assembly object reference
      report_name: report name generated by KBaseReport
      report_ref: report reference generated by KBaseReport
    */
    funcdef extract_binned_contigs_as_assembly(ExtractBinAsAssemblyParams params)
        returns (ExtractBinAsAssemblyResult returnVal) authentication required;

};
