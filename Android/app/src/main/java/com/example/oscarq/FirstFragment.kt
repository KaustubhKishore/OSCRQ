package com.example.oscarq

import android.content.Intent
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
import androidx.fragment.app.Fragment
import androidx.navigation.fragment.findNavController

class FirstFragment : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val intent = Intent(this, security::class.java)
        startActivity(intent)
    }
}

//    un onCreateView(
//        inflater: LayoutInflater,
//        container: ViewGroup?,
//        savedInstanceState: Bundle?
//    ): Intent {
////        inflater: LayoutInflater, container: ViewGroup?,
////        savedInstanceState: Bundle?
////    ): View? {
////        val a: CoordinatorLayout = findViewById(R.id.hideme)
////        a.visibility = View.GONE
//        // Inflate the layout for this fragment
//        val intent = Intent(this.activity, MainActivity::class.java)
//        startActivity(intent)
////
////       return inflater.inflate(R.layout.activity_main, container, false)
//
//    return intent
//    }
//
////    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
////        super.onViewCreated(view, savedInstanceState)
////        view.findViewById<Button>(R.id.button_first).setOnClickListener {
////            findNavController().navigate(R.id.action_FirstFragment_to_SecondFragment)
////        }
////    }
//}
