import weka.clusterers.HierarchicalClusterer;
import weka.core.Instances;
import weka.core.converters.ConverterUtils.DataSource;

public class Clustering02 {
    private final static String dataset = "C:\\Python\\Algorithm\\School\\clustering\\data07.arff";

    public static void main(String args[]) throws Exception{
        DataSource source = new DataSource(dataset);
        Instances data = source.getDataSet();
        HierarchicalClusterer model = new HierarchicalClusterer();

        model.setNumClusters(5);
        model.buildClusterer(data);
        System.out.println(model.graph());
    }
}
