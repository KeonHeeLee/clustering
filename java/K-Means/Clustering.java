import weka.clusterers.ClusterEvaluation;
import weka.clusterers.SimpleKMeans;
import weka.core.Instances;
import weka.core.converters.ConverterUtils.DataSource;

public class Clustering {
    private final static String dataset = "<test>.arff";

    public static void main(String args[]) throws Exception{
        DataSource source = new DataSource(dataset);
        Instances data = source.getDataSet();
        SimpleKMeans model = new SimpleKMeans();
        ClusterEvaluation clsEval = new ClusterEvaluation();

        model.setNumClusters(5);
        model.buildClusterer(data);
        System.out.println(model);

        clsEval.setClusterer(model);
        clsEval.evaluateClusterer(data);
        System.out.println("# of clusters: " + clsEval.getNumClusters());

    }
}
