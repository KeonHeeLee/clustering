package cluster;

import weka.clusterers.ClusterEvaluation;
import weka.clusterers.MakeDensityBasedClusterer;
import weka.core.Instances;
import weka.core.converters.ConverterUtils.DataSource;

public class Clustering03 {
    private final static String dataset = "C:\\Python\\Algorithm\\School\\clustering\\data07.arff";

    public static void main(String args[]) throws Exception{
        DataSource source = new DataSource(dataset);
        Instances data = source.getDataSet();
        MakeDensityBasedClusterer model = new MakeDensityBasedClusterer();
        ClusterEvaluation clsEval = new ClusterEvaluation();

        model.setMinStdDev(20);
        long start = System.currentTimeMillis();
        model.buildClusterer(data);
        long end = System.currentTimeMillis();
        System.out.println( "Executing Time : " + ( end - start )/1000.0 );
        System.out.println(model);

        clsEval.setClusterer(model);
        clsEval.evaluateClusterer(data);
        System.out.println("# of clusters: " + clsEval.getNumClusters());
    }
}
