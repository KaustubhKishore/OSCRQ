package com.example.oscarq

// Import the required libraries
import android.graphics.Color
import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.google.android.material.snackbar.Snackbar
import kotlinx.android.synthetic.main.activity_main2.*
import org.eazegraph.lib.charts.PieChart
import org.eazegraph.lib.models.PieModel


class Main2Activity : AppCompatActivity() {

    lateinit var tvR: TextView
    lateinit var tvPython:TextView
    lateinit var tvCPP:TextView
    lateinit var tvJava:TextView
    lateinit var pieChart: PieChart

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main2)
        setSupportActionBar(toolbar)

        // Link those objects with their
        // respective id's that
        // we have given in .XML file
        tvR = findViewById(R.id.tvR);
        tvPython = findViewById(R.id.tvPython);
        tvCPP = findViewById(R.id.tvCPP);
        tvJava = findViewById(R.id.tvJava);
        pieChart = findViewById(R.id.piechart);

        // Creating a method setData()
        // to set the text in text view and pie chart
        setData();

        fab.setOnClickListener { view ->
            Snackbar.make(view, "Welcome to OSCARQ! We are all about meaningful metrics. Visit our website for more.", Snackbar.LENGTH_INDEFINITE)
                .setAction("Action", null).show()
        }
    }

    private fun setData() {

        // Set the percentage of language used
        tvR.text = Integer.toString(40)
        tvPython.text = Integer.toString(30)
        tvCPP.text = Integer.toString(5)
        tvJava.text = Integer.toString(25)

        // Set the data and color to the pie chart
        pieChart.addPieSlice(
            PieModel(
                "R", tvR.text.toString().toInt().toFloat(),
                Color.parseColor("#FFA726")
            )
        )
        pieChart.addPieSlice(
            PieModel(
                "Python", tvPython.text.toString().toInt().toFloat(),
                Color.parseColor("#66BB6A")
            )
        )
        pieChart.addPieSlice(
            PieModel(
                "C++", tvCPP.text.toString().toInt().toFloat(),
                Color.parseColor("#EF5350")
            )
        )
        pieChart.addPieSlice(
            PieModel(
                "Java", tvJava.text.toString().toInt().toFloat(),
                Color.parseColor("#29B6F6")
            )
        )

        // To animate the pie chart
        pieChart.startAnimation()
    }

}
