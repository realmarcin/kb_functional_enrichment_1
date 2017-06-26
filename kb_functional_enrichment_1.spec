/*
A KBase module: kb_functional_enrichment_1
*/

module kb_functional_enrichment_1 {
    /* A boolean - 0 for false, 1 for true.
        @range (0, 1)
    */
    typedef int boolean;

    /* An X/Y/Z style reference
    */
    typedef string obj_ref;

    /*
      required params:
      genome_ref: Genome object reference
      workspace_name: the name of the workspace it gets saved to

      optional params:
      num_threads: number of threads
      
    */
    typedef structure{
        obj_ref genome_ref;
        string workspace_name;

        int num_threads;
    } FEOneInput;

    /*
        result_directory: folder path that holds all files generated by run_deseq2_app
        report_name: report name generated by KBaseReport
        report_ref: report reference generated by KBaseReport
    */
    typedef structure{
        string result_directory;
        string report_name;
        string report_ref;
    }FEOneResult;


    /*  
        run_fe1: run functional enrichment one

    */
    funcdef run_fe1(FEOneInput params)
        returns (FEOneResult returnVal) authentication required;
};
