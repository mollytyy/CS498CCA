package edu.illinois.storm;

import org.apache.storm.topology.BasicOutputCollector;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseBasicBolt;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Tuple;
import org.apache.storm.tuple.Values;

import java.util.HashMap;
import java.util.Map;

/** a bolt that tracks word count */
public class WordCountBolt extends BaseBasicBolt {
  // Hint: Add necessary instance variables if needed

  @Override
  public void execute(Tuple tuple, BasicOutputCollector collector) {
    /* ----------------------TODO-----------------------
    Task: word count
		Hint: using instance variable to tracking the word count
    ------------------------------------------------- */

		// End
  }

  @Override
  public void declareOutputFields(OutputFieldsDeclarer declarer) {
    /* ----------------------TODO-----------------------
    Task: declare output fields
    ------------------------------------------------- */

		// End
  }
}
